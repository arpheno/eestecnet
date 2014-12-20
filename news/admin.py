from django.contrib import admin
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget

from news.models import Entry, Membership


class MyEntryAdminForm(ModelForm):
    class Meta:
        model = Entry
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'en', 'iframe': 'true',
                                                      'css':
                                                          "/static/enet/css/wysiwyg"
                                                          ".css"}),
        }


class MembershipAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(MembershipAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            return qs.filter(team__in=request.user.teams_administered)
        except:
            return qs.none()


class MyEntryAdmin(admin.ModelAdmin):
    form = MyEntryAdminForm
    readonly_fields = ['published']
    list_display = ['pub_date', 'authors', 'headline', 'published']
    actions = ['publish_selected']

    def publish_selected(self, request, queryset):
        if request.user.is_superuser:
            rows_updated = queryset.update(published=True)
            if rows_updated == 1:
                message_bit = "1 story was"
            else:
                message_bit = "%s stories were" % rows_updated
            self.message_user(request,
                              "%s successfully marked as published." % message_bit)
        else:
            self.message_user(request,
                              "You lack the privileges to publish the news. One of the admins will review it and publish it")

    def get_queryset(self, request):
        qs = super(MyEntryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Usually a User can only add his or her own Events
        return qs.filter(author__in=request.user.teams.all())

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """ A Local admin will only be able to create :class:`Event`s for
         :class:`Member`s that he has privileges for. Admins still get to see all
         events"""
        if request.user.is_superuser:
            return super(MyEntryAdmin, self).formfield_for_manytomany(db_field, request,
                                                                      **kwargs)
        if db_field.name == "author":
            kwargs["queryset"] = request.user.teams_administered().all()
        return super(MyEntryAdmin, self).formfield_for_manytomany(db_field, request,
                                                                  **kwargs)


admin.site.register(Entry,MyEntryAdmin)
admin.site.register(Membership, MembershipAdmin)

# Register your models here.
