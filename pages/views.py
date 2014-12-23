import asana
from asana.asana import AsanaAPI
from django.contrib import messages
from django.forms import ModelForm, TextInput, Textarea
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView
from extra_views import CreateWithInlinesView, InlineFormSet
from form_utils.forms import BetterModelForm
from eestecnet.settings_deploy import ASANA_API_KEY, EESTEC_ITT_WORKSPACE_ID, \
    FEEDBACK_PROJECT_ID

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
        widgets = {
            'email': TextInput(attrs={'placeholder': 'Your Email (optional)'}),
            'subject': TextInput(attrs={'placeholder': 'Subject'}),
            'content': Textarea( attrs={'cols':50,'placeholder': 'Details'}),
        }
        exclude = ['read']



class NewWebsiteFeedback(CreateWithInlinesView):
    model = WebsiteFeedback
    inlines = [WebsiteFeedbackInline]
    form_class = WebsiteFeedbackForm


    def get_success_url(self):
        return ("/")

    def forms_valid(self, form,inlines):
        feedback = form.save(commit=False)
        if self.request.user.is_authenticated():
            feedback.user = self.request.user
        asana_api = AsanaAPI(ASANA_API_KEY, debug=True)

        asana_api.create_task(
            name = feedback.subject,
            notes = feedback.content+"\n"+feedback.email,
            workspace=EESTEC_ITT_WORKSPACE_ID,
            projects=[FEEDBACK_PROJECT_ID])
        feedback.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Thank you for your feedback. We appreciate it.')
        return redirect("/")