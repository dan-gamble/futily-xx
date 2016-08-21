from django.core.management import BaseCommand
from django.db.models import Avg

from ...models import Club
from ....players.models import Player, SPECIAL_TYPES, TEAM_OF_THE_WEEK


class Command(BaseCommand):
    def handle(self, *args, **options):
        clubs = Club.objects.all()

        for club in clubs:
            players = club.player_set.all()

            # Average rating
            club.average_rating = '{0:.2f}'.format(list(
                players.aggregate(Avg('overall_rating')).values()
            )[0] or 0)

            # All players
            club.total_players = len(players)

            # All players who aren't rare, standard, or TOTW
            club.total_special = Player.objects.filter(
                club=club,
                player_type__in=SPECIAL_TYPES
            ).count()

            # All informs
            club.total_inform = Player.objects.filter(
                club=club,
                player_type=TEAM_OF_THE_WEEK
            ).count()

            # All golds
            club.total_gold = Player.objects.filter(
                club=club,
                quality='gold'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            # All silvers
            club.total_silver = Player.objects.filter(
                club=club,
                quality='silver'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            # All bronzes
            club.total_bronze = Player.objects.filter(
                club=club,
                quality='bronze'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            club.save()
