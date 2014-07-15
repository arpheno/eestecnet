from django.views.generic import DetailView

from pages.models import Page


class StaticPage(DetailView):
    model = Page

    def get_object(self, queryset=None):
        return Page.objects.get(url=self.kwargs['url'])
