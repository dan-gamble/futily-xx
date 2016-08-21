from django.core.management import BaseCommand
from django.db.models import Avg

from ...models import League
from ....players.models import Player, SPECIAL_TYPES, TEAM_OF_THE_WEEK


class Command(BaseCommand):
    def handle(self, *args, **options):
        leagues = League.objects.all()

        for league in leagues:
            players = league.player_set.all()

            # Average rating
            league.average_rating = '{0:.2f}'.format(list(
                players.aggregate(Avg('overall_rating')).values()
            )[0] or 0)

            # All players
            league.total_players = len(players)

            # All players who aren't rare, standard, or TOTW
            league.total_special = Player.objects.filter(
                league=league,
                player_type__in=SPECIAL_TYPES
            ).count()

            # All informs
            league.total_inform = Player.objects.filter(
                league=league,
                player_type=TEAM_OF_THE_WEEK
            ).count()

            # All golds
            league.total_gold = Player.objects.filter(
                league=league,
                quality='gold'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            # All silvers
            league.total_silver = Player.objects.filter(
                league=league,
                quality='silver'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            # All bronzes
            league.total_bronze = Player.objects.filter(
                league=league,
                quality='bronze'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            league.save()
