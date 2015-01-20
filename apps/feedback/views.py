# Create your views here.
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSet, UpdateWithInlinesView

from apps.events.models import Event, Participation, Application
from apps.feedback.forms import QuestionForm, QuestionSetForm, AnswerSetForm, AnswerForm
from apps.feedback.models import Question, Answer, QuestionSet, AnswerSet
from eestecnet.forms import DialogFormMixin


class QuestionInline(InlineFormSet):
    model = Question
    form_class = QuestionForm


class AnswerInline(InlineFormSet):
    model = Answer
    form_class = AnswerForm
    extra = 0
    can_delete = False

class FillOutQuestionaire(DialogFormMixin, UpdateWithInlinesView):
    form_title = "base/base.html"
    inlines = [AnswerInline, ]
    parent_template = "base/base.html"
    form_class = AnswerSetForm
    model = AnswerSet

    def get_object(self, queryset=None):
        try:
            q= Application.objects.get(applicant=self.request.user,
                                      target=Event.objects.get(slug=self.kwargs['slug']))
        except ObjectDoesNotExist:
            raise PermissionDenied
        return q.questionaire
    def forms_valid(self,form,inlines):
        form.instance.filled = True
        return super(FillOutQuestionaire,self).forms_valid(form,inlines)

    def get_success_url(self):
        return reverse_lazy('event', kwargs=self.kwargs)

class AnswerFeedback(DialogFormMixin, UpdateWithInlinesView):
    form_title = "base/base.html"
    inlines = [AnswerInline, ]
    parent_template = "base/base.html"
    form_class = AnswerSetForm
    model = AnswerSet

    def get_object(self, queryset=None):
        try:
            p = Participation.objects.get(participant=self.request.user,
                                      target=Event.objects.get(slug=self.kwargs['slug']))
        except ObjectDoesNotExist:
            raise PermissionDenied
        return p.feedback

    def get_success_url(self):
        return reverse_lazy('event', kwargs=self.kwargs)

class NewQuestionset(DialogFormMixin, CreateWithInlinesView):
    parent_template = "base/base.html"
    form_title = "base/base.html"
    inlines = [QuestionInline, ]
    form_class = QuestionSetForm
    model = QuestionSet
    can_add = True
    def get_success_url(self):
        return reverse_lazy('events')

    def dispatch(self, request, *args, **kwargs):
        if Group.objects.get(
                name="Local Admins") in request.user.groups.all() or \
                request.user.is_superuser:  # Todo
            return super(NewQuestionset, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
