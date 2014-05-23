from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from events.models import Event
class MyEventAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "organizing_committee":
            kwargs["queryset"] = request.user.priviledged.all()
        return super(MyEventAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    def get_queryset(self, request):
        qs = super(MyEventAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organizing_committee__in=request.user.members.all())
admin.site.register(Event, MyEventAdmin)
