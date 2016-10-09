from django.conf.urls import url

from .views import LeagueDetailView, LeagueListView

urlpatterns = [
    url(r'^$', LeagueListView.as_view(), name='league_list'),
    url(r'^(?P<slug>[-\w]+)/$', LeagueDetailView.as_view(), name='league_detail')
]
