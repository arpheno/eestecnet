from django.db.models import get_model
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
from account.forms import EestecerChangeForm, EestecerCreationForm

Eestecer = get_model('account', 'Eestecer')
Achievement = get_model('account', 'Achievement')


class EestecerAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','profile_picture')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = EestecerChangeForm
    add_form = EestecerCreationForm
    list_display = ('email', 'first_name', 'last_name', 'events_participated', 'last_event')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    def get_queryset(self, request):
        """ A Local adminstrator will only be able to modify :class:`Event`s that he has priviledges for.
        Admins still get to see all events"""
        qs = super(EestecerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.None()


# Re-register UserAdmin
admin.site.register(Eestecer, EestecerAdmin)
admin.site.register(Achievement)
