from cms import externals
from cms.apps.pages.models import Page
from django.contrib.contenttypes.models import ContentType
from django.test import RequestFactory, TestCase
from django.views.generic import ListView

from ...clubs.models import Club
from ...players.models import Player
from ..models import League, Leagues


class TestView(ListView):
    model = League


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

            self.league = League.objects.create(
                page=self.leagues,
                ea_id=1,
                name='England',
                name_abbr='England',
                slug='england'
            )

            self.club = Club.objects.create(
                ea_id=1,
                name='Club',
                name_abbr='Club',
                slug='club',
                league=self.league
            )

            self.player_1 = Player.objects.create(
                ea_id=1,
                first_name='Dan',
                last_name='Gamble',
                common_name='Dan Gamble',
                league=self.league
            )

            self.player_2 = Player.objects.create(
                ea_id=2,
                first_name='John',
                last_name='Doe',
                common_name='John Doe'
            )

    def test_unicode(self):
        self.assertEqual(str(self.leagues), 'Leagues')

    def test_absolute_url(self):
        self.assertEqual(self.league.get_absolute_url(), '/england/')

    def test_players(self):
        self.assertEqual(list(self.league.players()), [self.player_1])

    def test_clubs(self):
        self.assertEqual(list(self.league.clubs()), [self.club])
