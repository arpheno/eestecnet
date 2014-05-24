from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User, Group, Permission
from account.models import Eestecer
from events.models import Event
from members.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        widgets={'members': FilteredSelectMultiple('members',is_stacked=False)}
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['priviledged'].queryset = Eestecer.objects.filter(members__pk=self.instance.pk)


class MyMemberAdmin(admin.ModelAdmin):
    form=MemberForm
    def save_model(self, request, obj, form, change):
        # TODO Determine if user has been completely degraded to remove rights to admin
        # for usr in obj.members.all():
        #    if not usr.is_staff:
        #    for mmbr in Member.objects.all():
        obj.save() # Save before meddling with permissions
        import pdb;pdb.set_trace();
        for usr in obj.priviledged.all():
            usr.is_staff=True
            mygroup, created = Group.objects.get_or_create(name='Local Admins')
            import pdb;pdb.set_trace();
            if created:
                for perm in [
                    'add_entry', 'change_entry', 'delete_entry',
                    'add_event', 'change_event', 'delete_event',
                    'change_member']:
                    mygroup.permissions.add(Permission.objects.get(codename=perm))
                mygroup.save()
            usr.groups.add(mygroup)
            usr.save()
        obj.save()
    def get_queryset(self, request):
        qs = super(MyMemberAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Usually a User can only see their own Events
        return qs.filter(priviledged=request.user)


admin.site.register(Member,MyMemberAdmin)
