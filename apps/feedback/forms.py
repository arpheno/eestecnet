from django.forms import Textarea

from form_utils.forms import BetterModelForm

from apps.feedback.models import Question


class QuestionForm(BetterModelForm):
    class Meta:
        model = Question
        widgets = {
            'q': Textarea(attrs={'rows': '1'}),
        }


