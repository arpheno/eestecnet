
# Create your views here.
from django.views.generic import ListView

from news.models import Entry


class home(ListView):
    model = Entry
    template_name = 'enet/home.html'

    def get_queryset(self):
        return Entry.objects.filter(published=True).order_by('-pub_date')[:5]


class NewsList(ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(published=True).order_by('-pub_date')[:5]
