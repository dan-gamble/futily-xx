from django.conf.urls import url

from .views import NationDetailView, NationListView

urlpatterns = [
    url(r'^$', NationListView.as_view(), name='nation_list'),
    url(r'^(?P<slug>[-\w]+)/$', NationDetailView.as_view(), name='nation_detail')
]
