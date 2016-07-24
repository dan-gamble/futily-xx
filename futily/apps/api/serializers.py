from rest_framework import serializers

from futily.apps.leagues.models import League
from futily.apps.nations.models import Nation


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
