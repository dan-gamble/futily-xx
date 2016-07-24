import requests
from django.utils.text import slugify

from .nations.models import Nation


class Downloader(object):
    def __init__(self):
        self.base_url = 'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item'

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
            'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item' \
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
