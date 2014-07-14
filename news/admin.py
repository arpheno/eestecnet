from django.contrib import admin

from news.models import Entry


class MyEntryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyEntryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Usually a User can only add his or her own Events
        return qs.filter(author__in=request.user.members.all())

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """ A Local admin will only be able to create :class:`Event`s for
         :class:`Member`s that he has privileges for. Admins still get to see all
         events"""
        if request.user.is_superuser:
            return super(MyEntryAdmin, self).formfield_for_manytomany(db_field, request,
                                                                      **kwargs)
        if db_field.name == "author":
            kwargs["queryset"] = request.user.priviledged.all()
        return super(MyEntryAdmin, self).formfield_for_manytomany(db_field, request,
                                                                  **kwargs)


admin.site.register(Entry,MyEntryAdmin)

# Register your models here.
