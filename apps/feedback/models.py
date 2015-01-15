from django.db.models import *


class Question(Model):
    parent = ForeignKey('feedback.QuestionSet')
    q = TextField()


class Answer(Model):
    parent = ForeignKey('feedback.AnswerSet')
    q = ForeignKey('feedback.Question', null=True)
    a = TextField(blank=True, null=True)


class QuestionSet(Model):
    name = TextField(max_length=30)
    parents = ManyToManyField('self',
                              help_text="Which questionaires do you want to include",
                              null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class AnswerSet(Model):
    parent = ForeignKey('feedback.QuestionSet')

    def relation(self):
        return str(self.participation.participant) + " " + str(self.participation.target)
