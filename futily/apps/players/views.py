from django.db.models import Q
from django.utils.text import slugify
from rest_framework import filters, viewsets

from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('first_name', 'last_name', 'common_name')

    def get_queryset(self):
        query = self.request.query_params.get('query', None)

        qs = Player.objects.all()

        if query:
            qs = qs.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(common_name__icontains=query)
            )

        nation = self.request.query_params.get('nation', None)

        if nation:
            qs = qs.filter(nation__slug=slugify(nation))

        print(query, nation)

        return qs
