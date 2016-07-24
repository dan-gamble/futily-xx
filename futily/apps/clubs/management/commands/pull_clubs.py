from django.core.management import BaseCommand

from futily.apps.downloader import Downloader


class Command(BaseCommand):
    def handle(self, *args, **options):
        downloader = Downloader()
        nation_mapping = {
            'ea_item': 'nation',
            'model_mapping': {
                'name': 'name',
                'name_abbr': 'abbrName',
                'ea_id': 'id',
                'image': 'imgUrl'
            },
            'model_images': {
                'image_sm': 'small',
                'image_md': 'medium',
                'image_lg': 'large'
            }
        }

        downloader.build_clubs()
