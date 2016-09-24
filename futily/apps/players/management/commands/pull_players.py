from django.core.management import BaseCommand

from futily.utils.downloader import Downloader


class Command(BaseCommand):
    def handle(self, *args, **options):
        downloader = Downloader()

        downloader.build_players()
