from rest_framework import routers

from apps.accounts.views import MembershipViewSet, AccountViewSet
from apps.announcements.views import CareerOfferViewSet, AnnouncementViewSet, NewsViewSet
from apps.events.views import GroupViewSet, EventViewSet, TrainingViewSet, ExchangeViewSet, WorkshopViewSet, \
    TravelViewSet
from apps.prioritylists.views import PriorityListViewSet, PriorityViewSet
from apps.questionnaires.views import QuestionnaireViewSet, ResponseViewSet, AnswerViewSet
from apps.questionnaires.views import QuestionViewSet
from apps.teams.views import BaseTeamViewSet, InternationalTeamViewSet, CommitmentViewSet
from common.views import ImageViewSet, ContentViewSet

approuter = routers.DefaultRouter()
approuter.register(r'groups', GroupViewSet)
approuter.register(r'images', ImageViewSet)
approuter.register(r'content', ContentViewSet)
approuter.register(r'memberships', MembershipViewSet)
approuter.register(r'accounts', AccountViewSet)
approuter.register(r'announcements', AnnouncementViewSet)
approuter.register(r'news', NewsViewSet)
approuter.register(r'careers', CareerOfferViewSet)
approuter.register(r'teams', BaseTeamViewSet)
approuter.register(r'commitments', CommitmentViewSet)
approuter.register(r'internationalteams', InternationalTeamViewSet)
approuter.register(r'questionnaires', QuestionnaireViewSet)
approuter.register(r'questions', QuestionViewSet)
approuter.register(r'responses', ResponseViewSet)
approuter.register(r'answers', AnswerViewSet)
approuter.register(r'prioritylists', PriorityListViewSet)
approuter.register(r'priorities', PriorityViewSet)
approuter.register(r'events', EventViewSet)
approuter.register(r'training-sessions', TrainingViewSet)
approuter.register(r'exchanges', ExchangeViewSet)
approuter.register(r'workshops', WorkshopViewSet)
approuter.register(r'travel', TravelViewSet)

