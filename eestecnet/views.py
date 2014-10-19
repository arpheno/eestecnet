from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect
from mailqueue.models import MailerMessage

from eestecnet import *


def init(request):
    create_local_admins()
    create_eestec_lcs()
    create_eestec_teams()
    create_eestec_news()
    create_eestec_people()
    create_inktronics()
    create_positions_for_achievements()
    create_pages()
    create_stubs()
    return redirect("/")
def newsletter(request):
    try:
        validate_email( request.POST['mailsub'] )
    except ValidationError:
        return redirect("/")
    message=MailerMessage()
    message.subject = "add to newsletter"
    message.content="Dear VC-IA, please kindly add "+request.POST['mailsub']+"to the newsletter list."
    message.from_address = "noreply@eestec.net",
    message.to_address = "vc-ia@eestec.net"
    message.save()
    return redirect("/")


