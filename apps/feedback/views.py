# Create your views here.
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSet

from apps.events.models import Event
from apps.feedback.forms import QuestionForm
from apps.feedback.models import Question, Answer, QuestionSet
from eestecnet.forms import DialogFormMixin


class QuestionInline(InlineFormSet):
    model = Question
    form_class = QuestionForm


class AnswerInline(InlineFormSet):
    model = Answer


class NewQuestionset(DialogFormMixin, CreateWithInlinesView):
    parent_template = "base/base.html"
    form_title = "base/base.html"
    inlines = [QuestionInline, ]
    model = QuestionSet

    def get_success_url(self):
        return reverse_lazy('event', kwargs=self.kwargs)

    def dispatch(self, request, *args, **kwargs):
        subject = Event.objects.get(slug=kwargs['slug'])
        if request.user in subject.organizers.all() or request.user.is_superuser:  # Todo
            return super(NewQuestionset, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
