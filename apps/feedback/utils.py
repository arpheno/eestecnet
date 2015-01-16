from apps.feedback.models import AnswerSet, Answer


def create_answer_set(questionset):
    answers = AnswerSet.objects.create(parent=questionset)
    answers.save()
    for question in questionset.question_set.all():
        Answer.objects.create(parent=answers, q=question).save()
    return answers


