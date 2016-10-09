import json
import os
import requests

from django.conf import settings

from futily.apps.clubs.models import Club
from futily.apps.leagues.models import League
from futily.apps.nations.models import Nation, get_default_nations_feed
from futily.apps.players.models import PLAYER_POSITION_LINES, Player
from futily.utils.methods import normalize_unicode


class Downloader(object):
    def __init__(self):
        self.base_path = os.path.join(settings.BASE_ROOT, 'jsons')
        self.leagues_json = u'https://fifa15.content.easports.com/fifa/' \
                            'fltOnlineAssets/' \
                            'B488919F-23B5-497F-9FC0-CACFB38863D0/2016/fut/' \
                            'config/web/teamconfig.json'
        self.clubs_json = 'https://fifa15.content.easports.com/fifa/' \
                          'fltOnlineAssets/' \
                          'B488919F-23B5-497F-9FC0-CACFB38863D0/2016/fut/' \
                          'config/web/teamconfig.json'

    def get_total_pages(self):
        with open(os.path.join(self.base_path, 'file1.json')) as data_file:
            return json.load(data_file)['totalPages']

    # def get_crawlable_urls(self):
    #     total_pages = self.get_total_pages()
    #
    #     return [
    #         u'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item' \
    #         '?jsonParamObject=%7B%22page%22:{}%7D'.format(
    #             x
    #         ) for x in range(1, total_pages + 1)
    #     ]

    def build_nation_data(self, *args, **kwargs):
        # urls = kwargs.get('failed', self.get_crawlable_urls())
        nations = kwargs.get('data', [])
        # failed_urls = []

        for i in range(1, self.get_total_pages() + 1):
            with open(os.path.join(self.base_path, 'file{}.json'.format(i))) as data_file:
                data = json.load(data_file)

                print 'Got page {}'.format(i)

                items = data['items']

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
                        'page': get_default_nations_feed()
                    }

                    if nation_data not in nations:
                        nations.append(nation_data)

                        print 'Added nation {}'.format(normalize_unicode(nation['name']))

        return nations

    def build_nations(self):
        data = self.build_nation_data()
        created_nations = []

        for obj in data:
            nation, created = Nation.objects.get_or_create(**obj)

            if created:
                created_nations.append(nation)

                print u'Created Nation: {}'.format(nation)

        print len(created_nations)

        return

    def build_league_data(self, *args, **kwargs):  # pylint: disable=too-complex,too-many-locals
        # urls = kwargs.get('failed', self.get_crawlable_urls())
        leagues = kwargs.get('data', [])
        # failed_urls = []
        leagues_data = {}

        league_ut_page = requests.get(self.leagues_json)

        if league_ut_page.status_code == requests.codes.ok:
            leagues_json = league_ut_page.json()

            for league in leagues_json['Years']:
                if league['Year'] == '2016':
                    leagues_data = league['Leagues']

        for i in range(1, self.get_total_pages() + 1):
            with open(os.path.join(self.base_path, 'file{}.json'.format(i))) as data_file:
                data = json.load(data_file)

                print 'Got page {}'.format(i)

                items = data['items']

                for item in items:
                    league = item['league']

                    league_data = {
                        'name': normalize_unicode(league['name']),
                        'name_abbr': league['abbrName'],
                        'ea_id': league['id'],
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
                            except Exception as e:  # pylint: disable=broad-except
                                print e

                            league_data['nation'] = nation if nation else None

                            if league_data not in leagues:
                                print 'Paired League & Nation: {} - {}'.format(
                                    normalize_unicode(league_data['name']),
                                    league_data['nation'].normalized_name()
                                )

                                leagues.append(league_data)

        return leagues

    def build_leagues(self):
        data = self.build_league_data()
        created_leagues = []

        for obj in data:
            league, created = League.objects.get_or_create(**obj)

            if created:
                created_leagues.append(league)

                print u'Created League: {}'.format(league)

        print len(created_leagues)

        return

    def build_club_data(self, *args, **kwargs):  # pylint: disable=too-complex,too-many-locals
        # urls = kwargs.get('failed', self.get_crawlable_urls())
        clubs = kwargs.get('data', [])
        # failed_urls = []
        clubs_data = {}

        club_ut_page = requests.get(self.clubs_json)

        if club_ut_page.status_code == requests.codes.ok:
            clubs_json = club_ut_page.json()

            for club in clubs_json['Years']:
                if club['Year'] == '2016':
                    clubs_data = club['Teams']

        for i in range(1, self.get_total_pages() + 1):
            with open(os.path.join(self.base_path, 'file{}.json'.format(i))) as data_file:
                data = json.load(data_file)

                print 'Got page {}'.format(i)

                items = data['items']

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
                            except Exception as e:  # pylint: disable=broad-except
                                print e

                            club_data['league'] = league if league else None

                            if club_data not in clubs:
                                print u'Paired Club & League: {} - {}'.format(
                                    club_data['name'],
                                    club_data['league']
                                )

                                clubs.append(club_data)

        return clubs

    def build_clubs(self):
        data = self.build_club_data()
        created_clubs = []

        for obj in data:
            club, created = Club.objects.get_or_create(**obj)

            if created:
                created_clubs.append(club)

                print u'Created Club: {}'.format(club)

        print len(created_clubs)

        return

    def build_player_data(self, *args, **kwargs):  # pylint: disable=too-many-locals
        # urls = kwargs.get('failed', self.get_crawlable_urls())
        players = kwargs.get('data', [])
        # failed_urls = []

        for i in range(1, self.get_total_pages() + 1):
            with open(os.path.join(self.base_path, 'file{}.json'.format(i))) as data_file:
                data = json.load(data_file)

                print 'Got page {}'.format(i)

                items = data['items']

                for item in items:
                    player = item

                    if player['commonName']:
                        common_name = player['commonName']
                    elif player['name']:
                        common_name = player['name']
                    else:
                        common_name = '{} {}'.format(
                            player['firstName'],
                            player['lastName']
                        )

                    for k, v in PLAYER_POSITION_LINES.items():  # pylint: disable=unused-variable
                        if player['position'] in PLAYER_POSITION_LINES[k]:
                            position_line = k

                    club = Club.objects.filter(ea_id=player['club']['id'])
                    league = club.first().league if club else None
                    nation = Nation.objects.filter(ea_id=player['nation']['id'])

                    player_data = {
                        'first_name': player['firstName'],
                        'last_name': player['lastName'],
                        'common_name': common_name,
                        'club': club.first() if club else None,
                        'league': league,
                        'nation': nation.first() if nation else None,
                        'image': player['headshotImgUrl'],
                        'image_sm': player['headshot']['smallImgUrl'],
                        'image_md': player['headshot']['medImgUrl'],
                        'image_lg': player['headshot']['largeImgUrl'],
                        'image_special_totw_md': player['specialImages']['medTOTWImgUrl'],
                        'image_special_totw_lg': player['specialImages']['largeTOTWImgUrl'],
                        'position': player['position'],
                        'position_full': player['positionFull'],
                        'position_line': position_line,
                        'playstyle': player['playStyle'],
                        'playstyle_id': player['playStyleId'],
                        'height': player['height'],
                        'weight': player['weight'],
                        'date_of_birth': player['birthdate'],
                        'acceleration': player['acceleration'],
                        'aggression': player['aggression'],
                        'agility': player['agility'],
                        'balance': player['balance'],
                        'ball_control': player['ballcontrol'],
                        'crossing': player['crossing'],
                        'curve': player['curve'],
                        'dribbling': player['dribbling'],
                        'finishing': player['finishing'],
                        'free_kick_accuracy': player['freekickaccuracy'],
                        'gk_diving': player['gkdiving'],
                        'gk_handling': player['gkhandling'],
                        'gk_kicking': player['gkkicking'],
                        'gk_positioning': player['gkpositioning'],
                        'gk_reflexes': player['gkreflexes'],
                        'heading_accuracy': player['headingaccuracy'],
                        'interceptions': player['interceptions'],
                        'jumping': player['jumping'],
                        'long_passing': player['longpassing'],
                        'long_shots': player['longshots'],
                        'marking': player['marking'],
                        'penalties': player['penalties'],
                        'positioning': player['positioning'],
                        'potential': player['potential'],
                        'reactions': player['reactions'],
                        'short_passing': player['shortpassing'],
                        'shot_power': player['shotpower'],
                        'sliding_tackle': player['slidingtackle'],
                        'sprint_speed': player['sprintspeed'],
                        'standing_tackle': player['standingtackle'],
                        'stamina': player['stamina'],
                        'strength': player['strength'],
                        'vision': player['vision'],
                        'volleys': player['volleys'],
                        'foot': player['foot'],
                        'skill_moves': player['skillMoves'],
                        'weak_foot': player['weakFoot'],
                        'traits': player['traits'],
                        'specialities': player['specialities'],
                        'workrate_att': player['atkWorkRate'],
                        'workrate_def': player['defWorkRate'],
                        'player_type': player['playerType'],
                        'item_type': player['itemType'],
                        'rating': player['rating'],
                        'card_att_1': player['attributes'][0]['value'],
                        'card_att_2': player['attributes'][1]['value'],
                        'card_att_3': player['attributes'][2]['value'],
                        'card_att_4': player['attributes'][3]['value'],
                        'card_att_5': player['attributes'][4]['value'],
                        'card_att_6': player['attributes'][5]['value'],
                        'quality': player['quality'],
                        'color': player['color'],
                        'is_gk': player['isGK'],
                        'is_special_type': player['isSpecialType'],
                        'is_loan': player['isLoan'],
                        'model_name': player['modelName'],
                        'base_id': player['baseId'],
                        'ea_id': player['baseId']
                    }

                    if player_data not in players:
                        players.append(player_data)

        return players

    def build_players(self):
        data = self.build_player_data()
        created_players = []

        for obj in data:
            player, created = Player.objects.get_or_create(**obj)

            if created:
                print u'Created Player: {}'.format(player)

        print len(created_players)

        return
