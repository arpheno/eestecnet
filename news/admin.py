from django.contrib import admin

from news.models import Entry


class MyEntryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyEntryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Usually a User can only add his or her own Events
        return qs.filter(author__in=request.user.members.all())


admin.site.register(Entry,MyEntryAdmin)

# Register your models here.
