from datetime import datetime
from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User, Group, Permission
from account.models import Eestecer
from events.models import Event
from members.models import Member, MemberImage, Commitment, Team


class MemberInline(admin.TabularInline):
    """ Inline Widget to display the Members of the Member with relevant information"""
    model = Member.members.through
    """ The model that is used"""
    readonly_fields = ['name','number_of_events','last_event']
    """The fields we want to display"""
    exclude = ['eestecer']
    """Exclude eestecer, or we end up being able to change things which we should not"""
    verbose_name_plural = "Members"
    """The title of the widget"""
    verbose_name = "pax"
    #todo get rid of event_eestecer object
    def name(self, instance):
        """ Returns the User's full name"""
        return instance.eestecer.first_name + instance.eestecer.last_name
    def last_event(self,instance):
        """Returns the last time a User went to an :class:`events.models.Event`"""
        return instance.eestecer.last_event()
    def number_of_events(self,instance):
        """Returns the amount of times a User participated in :class:`Events <events.models.Event>`"""
        return instance.eestecer.events_participated()
    def has_add_permission(self, request):
        """This is important so admins can't mess around"""
        return False

class MemberForm(forms.ModelForm):
    class Meta:
        widgets={'members': FilteredSelectMultiple('members',is_stacked=False)}
    def __init__(self, *args, **kwargs):
        """Make sure only members of the Member can get privileges"""
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['priviledged'].queryset = Eestecer.objects.filter(members__pk=self.instance.pk)
    def clean(self):
        """Put all priviledged members local admin rights"""
        priviledged = list(self.cleaned_data['priviledged'])
        for usr in priviledged:
            usr.is_staff=True
            mygroup, created = Group.objects.get_or_create(name='Local Admins')
            if created:
                #TODO put this in initial data for DB
                """If the group does not exist, create it"""
                for perm in [
                    'add_entry', 'change_entry', 'delete_entry',
                    'add_event', 'change_event', 'delete_event',
                    'add_application', 'change_application', 'delete_application',
                    'add_eestecer', # This is necessary so local admins can see their members
                    'change_member']:
                    mygroup.permissions.add(Permission.objects.get(codename=perm))
                mygroup.save()
            usr.groups.add(mygroup)
            usr.save()
        return self.cleaned_data
class MemberImageInline(admin.TabularInline):
    model = MemberImage

class MyMemberAdmin(admin.ModelAdmin):
    """A custom Admin displaying additional Member specific information"""
    form=MemberForm
    readonly_fields = ['member_count',]
    exclude = ['members']
    inlines = [MemberImageInline, MemberInline,]
    def save_model(self, request, obj, form, change):
        """ If the Member was just created, create a recruitment Event for it"""
        obj.save()
        if not change:
            a=Event.objects.create(
                name="Recruitment",
                scope="local",
                category="operational",
                summary="Interested in joining? Apply here or click for more information",
                description="We are always recruiting and welcoming new people.",
                start_date=datetime.now()
            )
            a.save()
            a.organizing_committee=[obj]

    def get_queryset(self, request):
        """If the modifying User is not an Admin, only show them their own Members"""
        qs = super(MyMemberAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(priviledged=request.user)

admin.site.register(Commitment,MyMemberAdmin)
admin.site.register(Team,MyMemberAdmin)
