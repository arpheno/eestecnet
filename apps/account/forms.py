import random
import string

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ImageField
from form_utils.widgets import ImageWidget


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
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
        fields = (
            "first_name", "middle_name", "last_name", "second_last_name",
            "thumbnail",
            "email", "gender")
    def save(self, commit=True):
        return super(EestecerCreationForm, self).save(commit=False)

class EestecerChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    thumbnail = ImageField(widget=ImageWidget())

    def __init__(self, *args, **kargs):
        super(EestecerChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Eestecer