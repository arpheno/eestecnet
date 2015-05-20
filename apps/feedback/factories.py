import factory
from apps.feedback.models import Question, Answer, AnswerSet, QuestionSet

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class LegacyQuestionSetFactory(factory.DjangoModelFactory):
    class Meta:
        model = QuestionSet
    name = "LOL"
    official=False
    category="feedback"

class LegacyQuestionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Question
    parent = factory.SubFactory(LegacyQuestionSetFactory)
    q = "WHATSYOURPROBLEM"


class LegacyAnswerSetFactory(factory.DjangoModelFactory):
    class Meta:
        model = AnswerSet
    parent = factory.SubFactory(LegacyQuestionSetFactory)
    filled=True


class LegacyAnswerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Answer
    parent = factory.SubFactory(LegacyAnswerSetFactory)
    q = factory.SubFactory(LegacyQuestionFactory)
    a = "THATSMYPROBLEM"




