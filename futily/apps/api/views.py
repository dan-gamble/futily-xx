from rest_framework import viewsets

from futily.apps.nations.models import Nation

from .serializers import NationSerializer


class NationViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Nation.objects.all()
    lookup_field = 'slug'
    serializer_class = NationSerializer
