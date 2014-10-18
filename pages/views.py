from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from pages.models import Page, Stub


class StaticPage(DetailView):
    model = Page

    def get_object(self, queryset=None):
        return get_object_or_404(Page, url=self.kwargs['url'])


class Documents(DetailView):
    model = Page

    def get_object(self, queryset=None):
        return get_object_or_404(Page, url='documents')


class AboutStubs(ListView):
    model = Stub
    queryset = Stub.objects.filter(group="about")


class ActivityStubs(ListView):
    model = Stub
    queryset = Stub.objects.filter(group="activities")

