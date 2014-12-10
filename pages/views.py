from django.contrib import messages
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView
from extra_views import CreateWithInlinesView, InlineFormSet
from form_utils.forms import BetterModelForm

from news.widgets import EESTECEditor
from pages.models import Page, Stub, WebsiteFeedback, WebsiteFeedbackImage


class StaticPage(DetailView):
    model = Page

    def get_object(self, queryset=None):
        return get_object_or_404(Page, url=self.kwargs['url'])


class DescriptionForm(ModelForm):
    class Meta:
        model = Page
        widgets = {'content': EESTECEditor(include_jquery=False)}


class StaticPageEdit(UpdateView):
    model = Page
    success_url = "/students"
    form_class = DescriptionForm

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


class WebsiteFeedbackInline(InlineFormSet):
    model = WebsiteFeedbackImage


class WebsiteFeedbackForm(BetterModelForm):
    class Meta:
        model = WebsiteFeedback
        exclude = ['read']


class NewWebsiteFeedback(CreateWithInlinesView):
    model = WebsiteFeedback
    inlines = [WebsiteFeedbackInline]
    form_class = WebsiteFeedbackForm

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user
        feedback.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Thank you for your feedback. We appreciate it.')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return ("/")