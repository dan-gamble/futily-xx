from rest_framework import viewsets

from futily.apps.nations.models import Nation
from futily.apps.leagues.models import League
from futily.apps.clubs.models import Club

from .serializers import ClubSerializer, LeagueSerializer, NationSerializer


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
