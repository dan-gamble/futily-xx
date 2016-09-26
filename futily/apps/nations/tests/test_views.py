from cms import externals
from cms.apps.pages.middleware import RequestPageManager
from cms.apps.pages.models import Page
from django.contrib.contenttypes.models import ContentType
from django.test import RequestFactory, TestCase
from django.views.generic import ListView

from ..models import Nation, Nations
from ..views import NationListView


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

    def test_nations_get_paginate_by(self):
        view = NationListView()
        view.request = self.factory.get('/')
        view.request.pages = RequestPageManager(view.request)

        self.assertEqual(view.get_paginate_by(None), 50)
