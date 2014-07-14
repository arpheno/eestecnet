import random
import string
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail import send_mail


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
        fields = ("email","first_name","middle_name","gender","last_name","second_last_name")
    def save(self, commit=True):
        user= super(EestecerCreationForm,self).save(commit=False)
        user.is_active=False
        user.activation_link=id_generator(30)
        send_mail(
            "An account was created at eestec.net with this email address. Please confirm your registration by visiting the link",
            "Go to\n http://test.eestec.net/complete/"+user.activation_link,
            "eestecnet@gmail.com",
            [user.email])
        user.save()

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