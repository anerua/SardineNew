from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

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
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    return render(request, "portfolio/index.html", {'form': form})
