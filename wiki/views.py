# Create your views here.
from django.views.generic import DetailView, UpdateView, CreateView, ListView

from wiki.forms import WikiForm
from wiki.models import WikiPage


class PageLatest(ListView):
    model = WikiPage
    template_name = 'wiki/latest.html'

    def get_queryset(self):
        return WikiPage.objects.order_by('-last_modified')[:5]


class PageRandom(DetailView):
    model = WikiPage

    def get_object(self, queryset=None):
        return WikiPage.objects.order_by('?')[0]

class WikiHome(DetailView):
    model = WikiPage
    def get_object(self, queryset=None):
        return WikiPage.objects.get(name="home")


class PageDetail(DetailView):
    model = WikiPage

    def get_object(self, queryset=None):
        page, created = WikiPage.objects.get_or_create(slug=self.kwargs['slug'])
        if created:
            page.name = page.slug
            page.save()
        return page


class PageUpdate(UpdateView):
    model = WikiPage
    form_class = WikiForm


class PageCreate(CreateView):
    model = WikiPage
    form_class = WikiForm
