from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.shortcuts import redirect


def newsletter(request):
    try:
        validate_email( request.POST['mailsub'] )
    except ValidationError:
        return redirect("/")
    send_mail("Dear VC-IA, please kindly add "+request.POST['mailsub']+"to the newsletter list.",
              "eestecnet@gmail.com",
              "vc-ia@eestec.net")
    return redirect("/")