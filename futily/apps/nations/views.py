from django.views.generic import DetailView, ListView

from .models import Nation


class NationListView(ListView):
    model = Nation
    paginate_by = 50


class NationDetailView(DetailView):
    model = Nation
