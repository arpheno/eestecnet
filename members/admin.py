from datetime import datetime
from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User, Group, Permission
from account.models import Eestecer
from events.models import Event
from members.models import Member, MemberImage


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

    def get_queryset(self, request):
        """If the modifying User is not an Admin, only show them their own Members"""
        qs = super(MyMemberAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(priviledged=request.user)

admin.site.register(Member,MyMemberAdmin)
