from rest_framework import serializers

from futily.apps.nations.models import Nation
from futily.apps.leagues.models import League
from futily.apps.clubs.models import Club
from futily.apps.players.models import Player


class NationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Nation


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    nation = NationSerializer()

    class Meta:
        model = League


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    league = LeagueSerializer()

    class Meta:
        model = Club


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    nation = NationSerializer()
    league = LeagueSerializer()
    club = ClubSerializer()

    class Meta:
        model = Player
