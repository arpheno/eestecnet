from django.db.models import *


class Question(Model):
    parent = ForeignKey('feedback.QuestionSet')
    q = TextField()

    class Meta:
        permissions = (('view_question', 'Can view question'),)
    def __str__(self):
        return self.q

    def __unicode__(self):
        return self.q


class Answer(Model):
    parent = ForeignKey('feedback.AnswerSet')
    q = ForeignKey('feedback.Question', null=True)
    a = TextField(blank=True, null=True)

    class Meta:
        permissions = (('view_answer', 'Can view answer'),)
    def __unicode__(self):
        return self.a

    def question(self):
        return self.q.question


class QuestionSet(Model):
    class Meta:
        permissions = (('view_questionset', 'Can view questionset'),)
    name = TextField(max_length=30)
    parents = ManyToManyField('self',
                              help_text="Which questionaires do you want to include",
                              null=True, blank=True, editable=False)

    official=BooleanField(default=False)
    category=CharField(choices=(("feedback","feedback"),("questionaire","questionaire")),max_length=30,default="feedback")
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class AnswerSet(Model):
    parent = ForeignKey('feedback.QuestionSet')
    filled=BooleanField(default=False,editable=False)

    class Meta:
        permissions = (('view_answerset', 'Can view answerset'),)
    def relation(self):
        return str(self.participation.participant) + " " + str(self.participation.target)
