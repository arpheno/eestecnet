from asana.asana import AsanaAPI
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.forms import ModelForm, TextInput, Textarea
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, UpdateView
from extra_views import CreateWithInlinesView, InlineFormSet
from form_utils.forms import BetterModelForm

from eestecnet.forms import DialogFormMixin
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


class NewWebsiteFeedback(DialogFormMixin, CreateWithInlinesView):
    model = WebsiteFeedback
    inlines = [WebsiteFeedbackInline]
    form_class = WebsiteFeedbackForm
    parent_template = "/"
    form_title = "What would you like to tell us?"
    submit = "Send feedback"
    action = "/pages/feedback/"

    def get_initial(self):
        initial = super(NewWebsiteFeedback, self).get_initial()
        if self.request.user.is_authenticated():
            initial["email"] = self.request.user.email
        return initial


    def get_success_url(self):
        return ""

    def forms_valid(self, form,inlines):
        feedback = form.save(commit=False)
        if self.request.user.is_authenticated():
            feedback.user = self.request.user
        asana_api = AsanaAPI(ASANA_API_KEY, debug=True)

        task = asana_api.create_task(
            name = feedback.subject,
            notes = feedback.content+"\n"+feedback.email,
            workspace=EESTEC_ITT_WORKSPACE_ID,
            projects=[FEEDBACK_PROJECT_ID])
        feedback.save()
        for inline in inlines:
            for form in inline:
                try:
                    screenshot = form.save(commit=False)
                    screenshot.entity = feedback
                    screenshot.save()
                    img = screenshot.image
                    asana_api.upload_attachment(task_id=task['id'],
                                                file_name="Screenshot.jpg",
                                                stream=screenshot.image)
                except:
                    pass
        messages.add_message(
            self.request,
            messages.INFO,
            'Thank you for your feedback. We appreciate it.')
        return redirect("/")


class Protected(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied
        return super(Protected, self).dispatch(request, *args, **kwargs)
