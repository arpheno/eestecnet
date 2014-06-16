from django import forms
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from django.db.models import ManyToManyField
from django.forms import Textarea
from account.models import Eestecer
from events.models import Event, Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application

    def clean(self):
        return self.cleaned_data


class ApplicationInline(admin.TabularInline):
    model = Application
    form = ApplicationForm
    readonly_fields = ["priority", "letter", "member_in", "applicant","gender"]
    def gender(self):
        return self.applicant.gender
    def has_add_permission(self, request):
        return False


class ParticipantInline(admin.TabularInline):
    model = Event.participants.through
    readonly_fields = ['name', 'food', 'passport_number','gender']
    exclude = ['eestecer']
    verbose_name_plural = "Participants"
    verbose_name = "pax"
    #todo get rid of event_eestecer object
    def name(self, instance):
        return instance.eestecer.first_name + instance.eestecer.last_name
    def gender(self,instance):
        return instance.eestecer.gender
    def food(self, instance):
        return instance.eestecer.food_preferences
    def passport_number(self, instance):
        return instance.eestecer.passport_number

    def has_add_permission(self, request):
        return False


class MyEventAdminForm(forms.ModelForm):
    class Meta:
        model = Event


class MyEventAdmin(admin.ModelAdmin):
    """ Custom interface to administrate Events from the django admin interface. """
    form = MyEventAdminForm
    list_display = ['OC','name']
    inlines = [ApplicationInline, ParticipantInline]
    """ Inline interface for displaying the applications to an event and making it possible to accept them"""
    """Interface to manage accepted participants, you can kick them out here again. TODO: penalties for leaving"""
    readonly_fields = ['participant_count']
    """ We exclude the participant count from being modified because its indirectly calculated by a method
     We exclude the participants from being modified because we accept participants through :class:`Application`s. """
    exclude = ['participants']
    #TODO Fieldsets

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """ A Local admin will only be able to create :class:`Event`s for
         :class:`Member`s that he has privileges for. Admins still get to see all events"""
        if request.user.is_superuser:
            return super(MyEventAdmin, self).formfield_for_manytomany(db_field, request,
                                                                      **kwargs)
        if db_field.name == "organizing_committee":
            kwargs["queryset"] = request.user.priviledged.all()
        return super(MyEventAdmin, self).formfield_for_manytomany(db_field, request,
                                                                  **kwargs)

    def get_queryset(self, request):
        """ A Local admin will only be able to modify :class:`Event`s that he has privileges for.
        Admins still get to see all events"""
        qs = super(MyEventAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organizing_committee__in=request.user.members.all())

    def save_related(self, request, form, formsets, change):
        """If there are accepted applications, we remove them and take action accordingly"""
        super(MyEventAdmin, self).save_related(request, form, formsets, change)
        myevent = Event.objects.get(name=form.cleaned_data["name"],organizing_committee=form.cleaned_data['organizing_committee'])
        for aplctn in myevent.application_set.filter(accepted=True):
            if myevent.name == "Recruitment":
                """If it concerns a recruitment event, put them into the LC"""
                myevent.organizing_committee.all()[0].members.add(aplctn.applicant)
            else:
                """Else just put them into the event"""
                myevent.participants.add(aplctn.applicant)
                #TODO send emails to participant, maybe make them confirm
            aplctn.delete()


class MyApplicationAdmin(admin.ModelAdmin):
    """ Custom interface to administrate Events from the django admin interface. """
    list_display = ['applicant', 'target', 'priority']
    list_editable = ['priority']
    #TODO Fieldsets

    def get_queryset(self, request):
        """ A Local admin will only be able to modify applications issued by members from their LC
        Admins still get to see all applications"""
        qs = super(MyApplicationAdmin, self).get_queryset(request)
        #if request.user.is_superuser:
        #TODO sanity check
        try:
            return qs.filter(applicant__in=request.user.members.filter(
                type__in=['observer', 'jlc', 'lc'])[0].members.all())
        except:
            return qs.none()


admin.site.register(Event, MyEventAdmin)
admin.site.register(Application, MyApplicationAdmin)
