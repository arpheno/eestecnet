from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from models import Eestecer

class EestecerCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(EestecerCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Eestecer
        fields = ("email","first_name","middle_name","last_name","second_last_name")

class EestecerChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(EestecerChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Eestecer