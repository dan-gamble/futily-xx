from django.views.generic import ListView

from ..views import EaDetailView
from .models import League


class LeagueListView(ListView):
    model = League
    paginate_by = 50

    def get_queryset(self):
        qs = super(LeagueListView, self).get_queryset()
        order_by = self.request.GET.get('order_by')

        if order_by:
            qs = qs.order_by(order_by)

        return qs

    def get_paginate_by(self, queryset):
        if self.request.GET.get('per_page'):
            return self.request.GET.get('per_page')
        else:
            return super(LeagueListView, self).get_paginate_by(queryset)


class LeagueDetailView(EaDetailView):
    model = League
