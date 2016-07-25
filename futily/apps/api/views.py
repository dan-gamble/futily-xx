from rest_framework import viewsets

from futily.apps.nations.models import Nation
from futily.apps.leagues.models import League
from futily.apps.clubs.models import Club
from futily.apps.players.models import Player

from .serializers import ClubSerializer, LeagueSerializer, NationSerializer, PlayerSerializer


class NationViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Nation.objects.all()
    lookup_field = 'slug'
    serializer_class = NationSerializer


class LeagueViewset(viewsets.ReadOnlyModelViewSet):
    queryset = League.objects.all()
    lookup_field = 'slug'
    serializer_class = LeagueSerializer


class ClubViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Club.objects.all()
    lookup_field = 'slug'
    serializer_class = ClubSerializer


class PlayerViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    lookup_field = 'slug'
    serializer_class = PlayerSerializer
