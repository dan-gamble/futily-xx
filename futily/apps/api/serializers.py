from rest_framework import serializers

from futily.apps.nations.models import Nation
from futily.apps.leagues.models import League
from futily.apps.clubs.models import Club
from futily.apps.players.models import Player


class NationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nation


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    nation = NationSerializer()

    class Meta:
        model = League
        # extra_kwargs = {
        #     'nation': {'lookup_field': 'slug'}
        # }


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    league = LeagueSerializer()

    class Meta:
        model = Club
        # extra_kwargs = {
        #     'league': {'lookup_field': 'slug'}
        # }


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    nation = NationSerializer()
    league = LeagueSerializer()
    club = ClubSerializer()

    class Meta:
        model = Player
        # extra_kwargs = {
        #     'nation': {'lookup_field': 'slug'},
        #     'league': {'lookup_field': 'slug'},
        #     'club': {'lookup_field': 'slug'}
        # }
