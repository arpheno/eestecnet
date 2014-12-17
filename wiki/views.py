# Create your views here.
from django.views.generic import DetailView, UpdateView, CreateView

from wiki.models import WikiPage


class WikiHome(DetailView):
    model = WikiPage

    def get_object(self, queryset=None):
        return WikiPage.objects.get(name="home")


class PageDetail(DetailView):
    model = WikiPage


class PageUpdate(UpdateView):
    model = WikiPage


class PageCreate(CreateView):
    model = WikiPage
