from rest_framework.serializers import ModelSerializer

from .models import Player


class PlayerSerializer(ModelSerializer):
    # club = ClubSerializer()
    # league = LeagueSerializer()
    # nation = NationSerializer()

    class Meta:
        depth = 0
        model = Player
        exclude = ('created', 'modified')
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
