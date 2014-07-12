import csv
from django import forms
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from django.db.models import ManyToManyField
from django.forms import Textarea
from django.http import HttpResponse
from suit_redactor.widgets import RedactorWidget
from account.models import Eestecer
from events.models import Event, Application, EventImage, \
  Participation, IncomingApplication, OutgoingApplication


class ApplicationInline(admin.TabularInline):
    model = Application
    readonly_fields = [ "priority", "letter", "member_in", "gender"]
    fields=[ "member_in","priority", "letter",  "gender",'accepted']
    def has_add_permission(self, request):
        return False
    def gender(self,instance):
        return self.instace.applicant.gender

class ParticipantInline(admin.TabularInline):
    model = Event.participants.through
    readonly_fields = ['e_mail', 'food', 't_shirt_size','confirmed']
    fields = ['e_mail', 'food', 't_shirt_size','confirmed']
    ordering = ['-confirmed']
    verbose_name_plural = "Participants"
    def e_mail(self, instance):
        return instance.participant.email
    def food(self, instance):
        return instance.participant.food_preferences
    def t_shirt_size(self, instance):
        return instance.participant.tshirt_size

    def has_add_permission(self, request):
        return False

class ImageInline(admin.TabularInline):
    model=EventImage
class MyEventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        widgets = {
            'summary': Textarea(attrs={'cols': 50, 'rows': 8}),
            'description': RedactorWidget(editor_options={'lang':'en','iframe':'true','css':"/static/enet/css/wysiwyg.css"}),
        }

class MyEventAdmin(admin.ModelAdmin):
    """ Custom interface to administrate Events from the django admin interface. """
    form = MyEventAdminForm
    list_display = ['OC','name']
    inlines = [ImageInline]
    """ Inline interface for displaying the applications to an event and making it possible to accept them"""
    exclude = ['participants',"participant_count"]
    fieldsets = (
        ('Basic Event Information', {
            'fields': (
                ('name'),('category'),('scope'),('summary','description'),
                ('participation_fee','max_participants'),'thumbnail'
            )
        }),
        ('Organizers', {
            'fields': (('organizing_committee','organizers'),)
        }),
        ('Dates', {
            'fields': (('start_date','end_date','deadline'),)
        }),
        ('Reports', {
            'classes':('collapse',),
            'fields': (('organizer_report','pax_report'),)
        })
    )
    add_fieldsets = (
        ('Basic Event Information', {
            'fields': (
                ('name','category','scope'),('summary','description'),
                ('participation_fee','max_participants'),'thumbnail'
            )
        }),
        ('Organizers', {
            'fields': (('organizing_committee','organizers'),)
        }),
        ('Dates', {
            'fields': (('start_date','end_date','deadline'),)
        }),
    )

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

class OutgoingApplicationFilter(admin.SimpleListFilter):#
    title = "Events"
    parameter_name = 'target'
    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        events=set([application.target for application in qs])
        for event in events:
            yield (event,event)
    def queryset(self, request, queryset):
        return queryset

class IncomingApplicationFilter(admin.SimpleListFilter):#
    title = "Events"
    parameter_name = 'target'
    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        events=set([application.target for application in qs])
        for event in events:
            yield (event,event)
    def queryset(self, request, queryset):
        return queryset

def get_own_members(request):
    return request.user.priviledged.filter( type__in=['observer', 'jlc', 'lc'])[0].members.all()

class OutgoingApplicationAdmin(admin.ModelAdmin):
    """ Custom interface to administrate Events from the django admin interface. """
    list_display = ['applicant', 'target', 'priority']
    list_editable = ['priority']
    list_filter = [OutgoingApplicationFilter,]
    def get_queryset(self, request):
        """ A Local admin will only be able to modify applications issued by members from their LC
        Admins still get to see all applications"""
        qs = super(OutgoingApplicationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            return qs.filter(applicant__in=get_own_members(request))
        except:
            return qs.none()


class IncomingApplicationAdmin(admin.ModelAdmin):
    """ Custom interface to administrate Events from the django admin interface. """
    list_display = ['applicant', 'target', 'priority','accepted']
    list_editable = ['accepted']
    list_filter = [IncomingApplicationFilter]
    #TODO Fieldsets

    def get_queryset(self, request):
        """ A Local admin will only be able to modify applications applying to an event by their LC
        Admins still get to see all applications"""
        qs = super(IncomingApplicationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            qs= qs.filter(target__in=request.user.priviledged.filter(
                type__in=['observer', 'jlc', 'lc'])[0].event_set.all())
        except:
            return qs.none()
        return qs

class EventParticipationAdmin(admin.ModelAdmin):
    """ Custom interface to administrate Events from the django admin interface. """
    list_display = ['participant','e_mail', 'food', 't_shirt_size','confirmed','transportation_details_filled']
    list_filter = [IncomingApplicationFilter]
    actions=['download_transportation_details']
    def download_participant_details(self,request,queryset):
        pass #todo
    def download_transportation_details(self,request,queryset):#todo test  #todo pdf instead of csv
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        for pax in queryset:
            writer.writerow([pax.get_full_name(),
                            pax.transportation.arrival,
                            pax.transportation.arrive_by,
                            pax.transportation.arrival_number,
                            pax.transportation.departure,
                            pax.transportation.depart_by])

        return response
    def transportation_details_filled(self,instance):
        if instance.transportation:
            return True
        return False
    #TODO Fieldsets
    def has_add_permission(self, request):
        return False
    def e_mail(self, instance):
        return instance.participant.email
    def food(self, instance):
        return instance.participant.food_preferences
    def t_shirt_size(self, instance):
        return instance.participant.tshirt_size
    def get_queryset(self, request):
        """ A Local admin will only be able to modify applications issued by members from their LC
        Admins still get to see all applications"""
        qs = super(EventParticipationAdmin, self).get_queryset(request)
        #if request.user.is_superuser:
        #TODO sanity check
        if request.user.is_superuser:
            return qs
        try:
            return qs.filter(target__in=request.user.priviledged.filter(
                type__in=['observer', 'jlc', 'lc'])[0].event_set.all())
        except:
            return qs.none()


admin.site.register(Event, MyEventAdmin)
admin.site.register(OutgoingApplication, OutgoingApplicationAdmin)
admin.site.register(IncomingApplication, IncomingApplicationAdmin)
admin.site.register(Participation, EventParticipationAdmin)
