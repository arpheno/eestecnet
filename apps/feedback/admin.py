# Register your models here.
from django.contrib import admin

from apps.feedback.models import QuestionSet, Question, Answer, AnswerSet


class QuestionAdmin(admin.TabularInline):
    model = Question


class QuestionsetAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin, ]
    model = QuestionSet


admin.site.register(QuestionSet, QuestionsetAdmin)


class AnswerAdmin(admin.TabularInline):
    model = Answer


class AnswersetAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin, ]
    model = AnswerSet
    list_display = ["relation", ]


admin.site.register(AnswerSet, AnswersetAdmin)
