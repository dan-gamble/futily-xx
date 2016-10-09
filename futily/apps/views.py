from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.views.generic import DetailView

from ..apps.players.models import Player
from ..apps.players.utils import PLAYER_LEVEL_SCHEMA, PLAYER_POSITION_SCHEMA, PLAYER_SORT_SCHEMA


class EaDetailView(DetailView):
    def pagination(self, queryset, page_count=28):
        # Create pagination for the players return
        paginator = Paginator(queryset, page_count)

        # Get the page from the URL
        page = self.request.GET.get('page')

        try:
            # Deliver the requested page
            pagination = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            pagination = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            pagination = paginator.page(paginator.num_pages)

        return pagination

    def get_context_data(self, **kwargs):
        context = super(EaDetailView, self).get_context_data()

        obj = self.get_object()
        model_name = type(obj).__name__

        # Creates club=club, league=league, etc.
        model_filters = {model_name.lower(): obj}

        # Grab all of the things we want to filter the players by
        get_filters = self.request.GET.dict()

        # Remove the page key as that is for pagination
        get_filters.pop('page', '')

        player_filters = {}

        for k, v in get_filters.items():
            if k == 'pos':
                if v == 'all':
                    # If the position is all we don't want to filter at all
                    pass
                elif v in PLAYER_POSITION_SCHEMA:
                    # If there are multiple positions
                    player_filters[PLAYER_POSITION_SCHEMA[v].items()[0][0]] = PLAYER_POSITION_SCHEMA[v].items()[0][1]
                else:
                    # If it's a singular position
                    player_filters['position__iexact'] = v
            if k == 'lvl':
                if v == 'all':
                    # If the level is all we don't want to filter at all
                    pass
                elif v in PLAYER_LEVEL_SCHEMA:
                    player_filters[PLAYER_LEVEL_SCHEMA[v].items()[0][0]] = PLAYER_LEVEL_SCHEMA[v].items()[0][1]

        players = Player.objects.filter(
            **model_filters
        ).select_related(
            'club', 'league', 'nation'
        )

        if player_filters:
            players = players.filter(**player_filters)

        if 'sort' in get_filters:
            players = players.order_by('-{}'.format(PLAYER_SORT_SCHEMA[get_filters['sort']]))

        context['players'] = self.pagination(players)

        return context
