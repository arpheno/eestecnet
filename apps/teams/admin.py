from django.contrib import admin

# Register your models here.
from apps.teams.models import Team, MemberImage, Board
from apps.news.models import Membership


class MemberInline(admin.TabularInline):
    """ Inline Widget to display the Members of the Member with relevant information"""
    model = Membership
    """ The model that is used"""
    readonly_fields = ['user', 'email', 'number_of_events', 'last_event']
    fields = ['user', 'email', 'privileged', 'board', 'number_of_events', 'last_event',
              'alumni']
    """The fields we want to display"""
    verbose_name_plural = "Members"
    """The title of the widget"""
    verbose_name = "pax"
    # todo get rid of event_eestecer object
    def name(self, instance):
        """ Returns the User's full name"""
        return instance.eestecer.first_name + instance.eestecer.last_name

    def last_event(self, instance):
        """Returns the last time a User went to an :class:`events.models.Event`"""
        return instance.eestecer.last_event()

    def number_of_events(self, instance):
        """Returns the amount of times a User participated in :class:`Events <events
        .models.Event>`"""
        return instance.eestecer.events_participated()

    def email(self, instance):
        return instance.eestecer.email

    def has_add_permission(self, request):
        """This is important so admins can't mess around"""
        return False


class MemberImageInline(admin.TabularInline):
    model = MemberImage


class MyMemberAdmin(admin.ModelAdmin):
    """A custom Admin displaying additional Member specific information"""
    readonly_fields = ['member_count', ]
    exclude = ['teams']
    inlines = [MemberImageInline, MemberInline, ]

    def get_queryset(self, request):
        """If the modifying User is not an Admin, only show them their own Members"""
        qs = super(MyMemberAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(users=request.user, membership__privileged=True)


admin.site.register(Team, MyMemberAdmin)
admin.site.register(Board)
