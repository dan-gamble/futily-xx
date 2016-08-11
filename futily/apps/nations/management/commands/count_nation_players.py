from django.core.management import BaseCommand
from django.db.models import Avg

from ...models import Nation
from ....players.models import Player, SPECIAL_TYPES


class Command(BaseCommand):
    def handle(self, *args, **options):
        nations = Nation.objects.all()

        for nation in nations:
            players = nation.player_set.all()

            # Average rating
            nation.average_rating = '{0:.2f}'.format(list(
                players.aggregate(Avg('overall_rating')).values()
            )[0] or 0)

            # All players
            nation.total_players = len(players)

            # All players who aren't rare or standard
            nation.total_special = Player.objects.filter(
                nation=nation,
                player_type__in=SPECIAL_TYPES
            ).count()

            # All golds
            nation.total_gold = Player.objects.filter(
                nation=nation,
                quality='gold'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            # All silvers
            nation.total_silver = Player.objects.filter(
                nation=nation,
                quality='silver'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            # All bronzes
            nation.total_bronze = Player.objects.filter(
                nation=nation,
                quality='bronze'
            ).exclude(
                player_type__in=SPECIAL_TYPES
            ).count()

            nation.save()
