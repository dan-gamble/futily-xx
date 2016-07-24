from rest_framework import serializers

from futily.apps.nations.models import Nation


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
