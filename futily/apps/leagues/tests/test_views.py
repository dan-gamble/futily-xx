from cms import externals
from cms.apps.pages.middleware import RequestPageManager
from cms.apps.pages.models import Page
from django.contrib.contenttypes.models import ContentType
from django.test import RequestFactory, TestCase

from ...players.models import Player
from ..models import League, Leagues
from ..views import LeagueDetailView, LeagueListView


class TestListView(LeagueListView):
    pass


class TestDetailView(LeagueDetailView):
    pass


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        with externals.watson.context_manager('update_index')():
            content_type = ContentType.objects.get_for_model(Leagues)

            self.page = Page.objects.create(
                title='Leagues',
                slug='leagues',
                content_type=content_type
            )

            self.leagues = Leagues.objects.create(
                page=self.page
            )

            self.league_1 = League.objects.create(
                page=self.leagues,
                ea_id=1,
                name='England',
                name_abbr='England',
                slug='england',
                average_rating=10.0,
                total_players=10,
                total_bronze=10,
                total_silver=10,
                total_gold=10,
                total_inform=10,
                total_special=10
            )

            self.league_2 = League.objects.create(
                page=self.leagues,
                ea_id=2,
                name='France',
                name_abbr='France',
                slug='france',
                average_rating=5.0,
                total_players=5,
                total_bronze=5,
                total_silver=5,
                total_gold=5,
                total_inform=5,
                total_special=5
            )

            self.player_1 = Player.objects.create(
                ea_id=1,
                first_name='Dan',
                last_name='Gamble',
                common_name='Dan Gamble',
                league=self.league_1
            )

            self.player_2 = Player.objects.create(
                ea_id=2,
                first_name='John',
                last_name='Doe',
                common_name='John Doe'
            )

    def test_list_view(self):
        view = default_list_view(self)

        self.assertEqual(view.request.pages.current.title, 'Leagues')

    def test_get_paginate_by(self):
        view = default_list_view(self)

        self.assertEqual(view.get_paginate_by(None), 50)

    def test_object_list(self):
        view = default_list_view(self)
        data = view.get_context_data()

        self.assertEqual(list(data['object_list']), [self.league_1, self.league_2])

        view = default_list_view(self, 1)
        data = view.get_context_data()

        self.assertEqual(list(data['object_list']), [self.league_1])

    def test_get_queryset(self):
        view = default_list_view(self)

        self.assertListEqual(list(view.get_queryset()), [self.league_1, self.league_2])

    def test_get_parameters(self):
        # Per page
        view = default_list_view(self)
        data = view.get_context_data()

        self.assertFalse(data['is_paginated'])
        self.assertListEqual(list(data['object_list']), [self.league_1, self.league_2])

        view = TestListView()
        view.request = self.factory.get('/', data={
            'per_page': 1
        })
        view.request.pages = RequestPageManager(view.request)
        view.object_list = League.objects.all()
        view.kwargs = {}

        data = view.get_context_data()

        self.assertTrue(data['is_paginated'])
        self.assertEqual(list(data['object_list']), [self.league_1])

        # Order by
        view = default_list_view(self)
        data = view.get_context_data()

        self.assertEqual(list(data['object_list']), [self.league_1, self.league_2])

        view_average_rating = default_list_view(self, data={'order_by': 'average_rating'})
        view_naverage_rating = default_list_view(self, data={'order_by': '-average_rating'})
        view_total_players = default_list_view(self, data={'order_by': 'total_players'})
        view_ntotal_players = default_list_view(self, data={'order_by': '-total_players'})
        view_total_bronze = default_list_view(self, data={'order_by': 'total_bronze'})
        view_ntotal_bronze = default_list_view(self, data={'order_by': '-total_bronze'})
        view_total_silver = default_list_view(self, data={'order_by': 'total_silver'})
        view_ntotal_silver = default_list_view(self, data={'order_by': '-total_silver'})
        view_total_gold = default_list_view(self, data={'order_by': 'total_gold'})
        view_ntotal_gold = default_list_view(self, data={'order_by': '-total_gold'})
        view_total_inform = default_list_view(self, data={'order_by': 'total_inform'})
        view_ntotal_inform = default_list_view(self, data={'order_by': '-total_inform'})
        view_total_special = default_list_view(self, data={'order_by': 'total_special'})
        view_ntotal_special = default_list_view(self, data={'order_by': '-total_special'})

        data_average_rating = view_average_rating.get_context_data()
        data_naverage_rating = view_naverage_rating.get_context_data()
        data_total_players = view_total_players.get_context_data()
        data_ntotal_players = view_ntotal_players.get_context_data()
        data_total_bronze = view_total_bronze.get_context_data()
        data_ntotal_bronze = view_ntotal_bronze.get_context_data()
        data_total_silver = view_total_silver.get_context_data()
        data_ntotal_silver = view_ntotal_silver.get_context_data()
        data_total_gold = view_total_gold.get_context_data()
        data_ntotal_gold = view_ntotal_gold.get_context_data()
        data_total_inform = view_total_inform.get_context_data()
        data_ntotal_inform = view_ntotal_inform.get_context_data()
        data_total_special = view_total_special.get_context_data()
        data_ntotal_special = view_ntotal_special.get_context_data()

        self.assertListEqual(list(data_average_rating['object_list']), [self.league_2, self.league_1])
        self.assertListEqual(list(data_naverage_rating['object_list']), [self.league_1, self.league_2])
        self.assertListEqual(list(data_total_players['object_list']), [self.league_2, self.league_1])
        self.assertListEqual(list(data_ntotal_players['object_list']), [self.league_1, self.league_2])
        self.assertListEqual(list(data_total_bronze['object_list']), [self.league_2, self.league_1])
        self.assertListEqual(list(data_ntotal_bronze['object_list']), [self.league_1, self.league_2])
        self.assertListEqual(list(data_total_silver['object_list']), [self.league_2, self.league_1])
        self.assertListEqual(list(data_ntotal_silver['object_list']), [self.league_1, self.league_2])
        self.assertListEqual(list(data_total_gold['object_list']), [self.league_2, self.league_1])
        self.assertListEqual(list(data_ntotal_gold['object_list']), [self.league_1, self.league_2])
        self.assertListEqual(list(data_total_inform['object_list']), [self.league_2, self.league_1])
        self.assertListEqual(list(data_ntotal_inform['object_list']), [self.league_1, self.league_2])
        self.assertListEqual(list(data_total_special['object_list']), [self.league_2, self.league_1])
        self.assertListEqual(list(data_ntotal_special['object_list']), [self.league_1, self.league_2])

    def test_detail_players(self):
        view = default_detail_view(self)
        view.object = self.league_1
        view.kwargs = {'slug': self.league_1.slug}
        data = view.get_context_data()

        self.assertListEqual(list(data['league'].players()), [self.player_1])


def default_list_view(obj, paginate_by=LeagueListView.paginate_by, data=None):
    if data is None:
        data = {}

    view = TestListView(paginate_by=paginate_by)
    view.request = obj.factory.get('/', data=data)
    view.request.pages = RequestPageManager(view.request)
    view.object_list = view.get_queryset()
    view.kwargs = {}

    return view


def default_detail_view(obj, url='/england/', data=None):
    if data is None:
        data = {}

    view = TestDetailView()
    view.request = obj.factory.get(url, data=data)
    view.request.pages = RequestPageManager(view.request)

    return view
