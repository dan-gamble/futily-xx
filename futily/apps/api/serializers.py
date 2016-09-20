from rest_framework import serializers

from futily.apps.nations.models import Nation
from futily.apps.leagues.models import League
from futily.apps.clubs.models import Club
from futily.apps.players.models import Player


class NationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Nation

    def __init__(self, *args, **kwargs):
        super(NationSerializer, self).__init__(*args, **kwargs)

        self.is_full = self.context['request'].query_params.get('full', False)

        if not self.is_full:
            base_fields = ['slug', 'name', 'image_sm']

            for field in self.fields:
                if field not in base_fields:
                    self.fields.pop(field)


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = League

    def __init__(self, *args, **kwargs):
        super(LeagueSerializer, self).__init__(*args, **kwargs)

        self.is_full = self.context['request'].query_params.get('full', False)

        self.fields['nation'] = NationSerializer(context=self.context)

        if not self.is_full:
            base_fields = ['slug', 'name']

            for field in self.fields:
                if field not in base_fields:
                    self.fields.pop(field)


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Club

    def __init__(self, *args, **kwargs):
        super(ClubSerializer, self).__init__(*args, **kwargs)

        self.is_full = self.context['request'].query_params.get('full', False)

        self.fields['league'] = LeagueSerializer(context=self.context)

        if not self.is_full:
            base_fields = ['slug', 'name', 'image_dark_sm']

            for field in self.fields:
                if field not in base_fields:
                    self.fields.pop(field)


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Player

    def __init__(self, *args, **kwargs):
        super(PlayerSerializer, self).__init__(*args, **kwargs)

        self.is_full = self.context['request'].query_params.get('full', False)

        # This allows us to pass the context to the foreign keys, we need this in every Serializer
        self.fields['nation'] = NationSerializer(context=self.context)
        self.fields['league'] = LeagueSerializer(context=self.context)
        self.fields['club'] = ClubSerializer(context=self.context)

        if not self.is_full:
            base_fields = ['nation', 'club', 'slug', 'common_name', 'image', 'position', 'quality', 'overall_rating',
                           'card_att_1', 'card_att_2', 'card_att_3', 'card_att_4', 'card_att_5', 'card_att_6']

            for field in self.fields:
                if field not in base_fields:
                    self.fields.pop(field)
