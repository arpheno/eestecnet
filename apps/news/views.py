
# Create your views here.
from django.views.generic import ListView, DetailView

from apps.news.models import Entry


class home(ListView):
    model = Entry
    template_name = 'base/home.html'

    def get_queryset(self):
        return Entry.objects.filter(category="news", published=True,
                                    front_page_news=True).order_by(
            '-pub_date')[:5]


class CarreerDetail(DetailView):
    model = Entry
    template_name = "news/carreer_detail.html"


class CarreerList(ListView):
    model = Entry
    template_name = "news/carreer_list.html"

    def get_queryset(self):
        return Entry.objects.filter(published=True, category="carreer").order_by(
            '-pub_date')

class NewsList(ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(published=True, category="news").order_by(
            '-pub_date')[:15]
