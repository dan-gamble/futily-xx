from django.views.generic import ListView

from ..views import EaDetailView
from .models import Nation


class NationListView(ListView):
    model = Nation
    paginate_by = 50

    def get_queryset(self):
        qs = super(NationListView, self).get_queryset()
        order_by = self.request.GET.get('order_by')

        if order_by:
            qs = qs.order_by(order_by)

        return qs

    def get_paginate_by(self, queryset):
        if self.request.GET.get('per_page'):
            return self.request.GET.get('per_page')
        else:
            return super(NationListView, self).get_paginate_by(queryset)


class NationDetailView(EaDetailView):
    model = Nation
