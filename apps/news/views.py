
# Create your views here.
from django.views.generic import ListView

from apps.news.models import Entry


class home(ListView):
    model = Entry
    template_name = 'base/home.html'

    def get_queryset(self):
        return Entry.objects.filter(published=True, front_page_news=True).order_by(
            '-pub_date')[:5]


class NewsList(ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(published=True).order_by('-pub_date')[:5]
