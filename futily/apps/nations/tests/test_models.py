from cms import externals
from cms.apps.pages.models import Page
from django.contrib.contenttypes.models import ContentType
from django.test import RequestFactory, TestCase
from django.views.generic import ListView

from ...players.models import Player
from ..models import Nation, Nations


class TestView(ListView):
    model = Nation


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        with externals.watson.context_manager('update_index')():
            content_type = ContentType.objects.get_for_model(Nations)

            self.page = Page.objects.create(
                title='Nations',
                slug='nations',
                content_type=content_type
            )

            self.nations = Nations.objects.create(
                page=self.page
            )

            self.nation = Nation.objects.create(
                page=self.nations,
                ea_id=1,
                name='England',
                name_abbr='England',
                slug='england'
            )

            self.player_1 = Player.objects.create(
                ea_id=1,
                first_name='Dan',
                last_name='Gamble',
                common_name='Dan Gamble',
                nation=self.nation
            )

            self.player_2 = Player.objects.create(
                ea_id=2,
                first_name='John',
                last_name='Doe',
                common_name='John Doe'
            )

    def test_nation_url(self):
        self.assertEqual(self.nation.get_absolute_url(), '/england/')

    def test_nation_players(self):
        self.assertEqual(list(self.nation.players()), [self.player_1])
