from django import forms
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from django.db.models import ManyToManyField
from django.forms import Textarea
from events.models import Event, Application
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
    def clean(self):
        return self.cleaned_data

class ApplicationInline(admin.TabularInline):
    model = Application
    form= ApplicationForm
    readonly_fields = ["priority", "letter", "member_in","applicant"]
    def has_add_permission(self, request):
        return False
class MyEventAdminForm(forms.ModelForm):
    class Meta:
        model = Event

class MyEventAdmin(admin.ModelAdmin):
    """ Custom interface to administrate Events from the django admin interface. """
    form = MyEventAdminForm
    inlines = [ApplicationInline, ]
    """ Inline interface for displaying the applications to an event and making it possible to accept them"""
    filter_horizontal = ['participants']
    """Interface to manage accepted participants, you can kick them out here again. TODO: penalties for leaving"""
    readonly_fields = ['participant_count']
    """ We exclude the participant count from being modified because its indirectly calculated by a method
     We exclude the participants from being modified because we accept participants through :class:`Application`s. """
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """ A Local adminstrator will only be able to create :class:`Event`s for
         :class:`Member`s that he has priviledges for. Admins still get to see all events"""
        if request.user.is_superuser:
            return super(MyEventAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name == "organizing_committee":
            kwargs["queryset"] = request.user.priviledged.all()
        c
        return super(MyEventAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def get_queryset(self, request):
        """ A Local adminstrator will only be able to modify :class:`Event`s that he has priviledges for.
        Admins still get to see all events"""
        qs = super(MyEventAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organizing_committee__in=request.user.members.all())

    def save_related(self, request, form, formsets, change):
        super(MyEventAdmin,self).save_related( request, form, formsets, change)
        myevent=Event.objects.get(name=form.cleaned_data["name"])
        for aplctn in myevent.application_set.filter(accepted=True):
            myevent.participants .add(aplctn.applicant)
            #TODO send emails to participant
            aplctn.delete()

admin.site.register(Event, MyEventAdmin)
admin.site.register(Application)
