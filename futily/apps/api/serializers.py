from rest_framework import serializers

from futily.apps.nations.models import Nation
from futily.apps.leagues.models import League
from futily.apps.clubs.models import Club


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
