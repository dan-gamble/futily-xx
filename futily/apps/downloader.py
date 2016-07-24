import requests
from django.utils.text import slugify

from futily.utils.methods import normalize_unicode

from .nations.models import Nation
from .leagues.models import League
from .clubs.models import Club


class Downloader(object):
    def __init__(self):
        self.base_url = u'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item'
        self.leagues_json = u'https://fifa15.content.easports.com/fifa/' \
                            'fltOnlineAssets/' \
                            'B488919F-23B5-497F-9FC0-CACFB38863D0/2016/fut/' \
                            'config/web/teamconfig.json'
        self.clubs_json = 'https://fifa15.content.easports.com/fifa/' \
                          'fltOnlineAssets/' \
                          'B488919F-23B5-497F-9FC0-CACFB38863D0/2016/fut/' \
                          'config/web/teamconfig.json'

    def get_total_pages(self):
        page = requests.get(self.base_url)

        if page.status_code == requests.codes.ok:
            try:
                page_json = page.json()
                return page_json['totalPages']
            except ValueError:
                print("Can't convert page to JSON")
        else:
            raise Exception("Couldn't get total page")

    def get_crawlable_urls(self):
        total_pages = self.get_total_pages()

        return [
            u'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item' \
            '?jsonParamObject=%7B%22page%22:{}%7D'.format(
                x
            ) for x in range(1, total_pages + 1)
        ]

    def build_nation_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        nations = kwargs.get('data', [])
        failed_urls = []

        for i, url in enumerate(urls):
            page = requests.get(url)

            if page.status_code == requests.codes.ok:
                try:
                    print 'Got page {}'.format(i)

                    page_json = page.json()
                    items = page_json['items']

                    for item in items:
                        nation = item['nation']

                        nation_data = {
                            'name': nation['name'],
                            'name_abbr': nation['abbrName'],
                            'ea_id': nation['id'],
                            'image_sm': nation['imageUrls']['small'],
                            'image_md': nation['imageUrls']['medium'],
                            'image_lg': nation['imageUrls']['large'],
                            'image': nation['imgUrl'],
                            'slug': slugify(nation['name'])
                        }

                        if nation_data not in nations:
                            nations.append(nation_data)

                            print 'Added nation {}'.format(nation_data['name'])

                except ValueError:
                    failed_urls.append(url)

                    print "Can't convert page to JSON"
            else:
                failed_urls.append(url)

                print 'Url failed: {}'.format(url)

            print failed_urls

        if failed_urls:
            self.build_nation_data(failed=failed_urls, data=nations)

        return nations

    def build_nations(self):
        data = self.build_nation_data()
        created_nations = []

        for obj in data:
            nation, created = Nation.objects.get_or_create(**obj)

            if created:
                created_nations.append(nation)

                print (u'Created Nation: {}'.format(nation))

        print len(created_nations)

        return

    def build_league_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        leagues = kwargs.get('data', [])
        failed_urls = []
        leagues_data = {}

        league_ut_page = requests.get(self.leagues_json)

        if league_ut_page.status_code == requests.codes.ok:
            leagues_json = league_ut_page.json()

            for league in leagues_json['Years']:
                if league['Year'] == '2016':
                    leagues_data = league['Leagues']

        for i, url in enumerate(urls):
            page = requests.get(url)

            if page.status_code == requests.codes.ok:
                print 'Got page {}'.format(i)

                page_json = page.json()
                items = page_json['items']

                for item in items:
                    league = item['league']

                    league_data = {
                        'name': normalize_unicode(league['name']),
                        'name_abbr': league['abbrName'],
                        'ea_id': league['id'],
                        'slug': slugify(league['name']),
                        'nation': None
                    }

                    for data in leagues_data:
                        league_id = int(data['LeagueId'])
                        scraped_id = int(league_data['ea_id'])
                        nation_id = int(data['NationId'])

                        if league_id == scraped_id:
                            try:
                                nation = Nation.objects.get(
                                    ea_id=nation_id
                                )
                            except Exception as e:
                                print e

                            league_data['nation'] = nation if nation else None

                            if league_data not in leagues:
                                print 'Paired League & Nation: {} - {}'.format(
                                    league_data['name'],
                                    league_data['nation']
                                )

                                leagues.append(league_data)
            else:
                failed_urls.append(url)

                print 'Url failed: {}'.format(url)

        if failed_urls:
            self.build_league_data(failed=failed_urls, data=leagues)

        return leagues

    def build_leagues(self):
        data = self.build_league_data()
        created_leagues = []

        for obj in data:
            league, created = League.objects.get_or_create(**obj)

            if created:
                created_leagues.append(league)

                print (u'Created League: {}'.format(league))

        print len(created_leagues)

        return

    def build_club_data(self, *args, **kwargs):
        urls = kwargs.get('failed', self.get_crawlable_urls())
        clubs = kwargs.get('data', [])
        failed_urls = []
        clubs_data = {}

        club_ut_page = requests.get(self.clubs_json)

        if club_ut_page.status_code == requests.codes.ok:
            clubs_json = club_ut_page.json()

            for club in clubs_json['Years']:
                if club['Year'] == '2016':
                    clubs_data = club['Teams']

        for i, url in enumerate(urls):
            page = requests.get(url)

            if page.status_code == requests.codes.ok:
                print 'Got page {}'.format(i)

                page_json = page.json()
                items = page_json['items']

                for item in items:
                    club = item['club']

                    club_data = {
                        'name': club['name'],
                        'name_abbr': club['abbrName'],
                        'ea_id': club['id'],
                        'image_dark_sm': club['imageUrls']['dark']['small'],
                        'image_dark_md': club['imageUrls']['dark']['medium'],
                        'image_dark_lg': club['imageUrls']['dark']['large'],
                        'image_normal_sm': club['imageUrls']['normal']['small'],
                        'image_normal_md': club['imageUrls']['normal']['medium'],
                        'image_normal_lg': club['imageUrls']['normal']['large'],
                        'slug': slugify(club['name']),
                        'league': None
                    }

                    for data in clubs_data:
                        club_id = int(data['TeamId'])
                        scraped_id = int(club_data['ea_id'])
                        league_id = int(data['LeagueId'])

                        if club_id == scraped_id:
                            try:
                                league = League.objects.get(
                                    ea_id=league_id
                                )
                            except Exception as e:
                                print e

                            club_data['league'] = league if league else None

                            if club_data not in clubs:
                                print u'Paired Club & League: {} - {}'.format(
                                    club_data['name'],
                                    club_data['league']
                                )

                                clubs.append(club_data)
            else:
                failed_urls.append(url)

                print 'Url failed: {}'.format(url)

        if failed_urls:
            self.build_club_data(failed=failed_urls, data=clubs)

        return clubs

    def build_clubs(self):
        data = self.build_club_data()
        created_clubs = []

        for obj in data:
            club, created = Club.objects.get_or_create(**obj)

            if created:
                created_clubs.append(club)

                print (u'Created Club: {}'.format(club))

        print len(created_clubs)

        return
