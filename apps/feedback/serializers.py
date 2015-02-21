from rest_framework import serializers

from apps.feedback.models import AnswerSet


class AnswerSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerSet
        fields = ('answer_set')



