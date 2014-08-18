from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from pages.models import Page


class StaticPage(DetailView):
    model = Page

    def get_object(self, queryset=None):
        return get_object_or_404(Page, url=self.kwargs['url'])
