from django.conf import settings
from rest_framework import viewsets
from rest_framework.settings import perform_import

from futily.apps.nations.models import Nation
from futily.apps.leagues.models import League
from futily.apps.clubs.models import Club
from futily.apps.players.models import Player
from futily.utils.pagination import CustomPagination

from .serializers import ClubSerializer, LeagueSerializer, NationSerializer, PlayerSerializer


class EaAssetViewset(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        qs = super(EaAssetViewset, self).get_queryset()
        query = self.request.query_params.get('query', None)
        order = self.request.query_params.get('order', None)

        if query:
            qs = qs.filter(
                name__icontains=query
            )

        if order:
            qs = qs.order_by('-{}'.format(order))

        return qs

    def list(self, request, *args, **kwargs):
        response = super(EaAssetViewset, self).list(request, args, kwargs)
        model = self.serializer_class.Meta.model
        # fields = self.serializer_class.Meta.model._meta.get_all_field_names()
        response.data['order_options'] = ['total_players', 'name', 'total_bronze', 'total_silver', 'total_gold',
                                          'total_inform', 'total_special', 'average_rating']

        default_order_by = model._meta.ordering[0]
        response.data['default_order_by'] = default_order_by if default_order_by[0] is not '-' else default_order_by[1:]

        return response



class NationViewset(EaAssetViewset):
    queryset = Nation.objects.all()
    lookup_field = 'slug'
    serializer_class = NationSerializer


class LeagueViewset(EaAssetViewset):
    queryset = League.objects.all()
    lookup_field = 'slug'
    serializer_class = LeagueSerializer


class ClubViewset(EaAssetViewset):
    queryset = Club.objects.all()
    lookup_field = 'slug'
    serializer_class = ClubSerializer


class PlayerViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    lookup_field = 'slug'
    serializer_class = PlayerSerializer
