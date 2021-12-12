from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm

import mimetypes, os

# Create your views here.
def index(request):
    if request.method == 'POST':
        print("I came here")
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Message from website"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']
            }
            if body['first_name'] == "":
                body['first_name'] = "Anonymous"
            if body['last_name'] == "":
                body['last_name'] = "Anonymous"
            
            message = f"First Name: {body['first_name']}\nLast Name: {body['last_name']}\nEmail: {body['email_address']}\n\n{body['message']}"

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    return render(request, "portfolio/index.html", {'form': form})


def download_resume(request):
    current_path = os.path.dirname(__file__)
    # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = "Martins_Anerua_Resume.pdf"
    fl_path = os.path.join(current_path, "static/portfolio/others/") + filename

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
