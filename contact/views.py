from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        return create_contact(request)
    else:
        return show_contact_form(request)

def create_contact(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact_form.html', {'form': form})

    send_contact_email(form.cleaned_data)
    
    contact = Contact(
        name=form.cleaned_data['name'],
        phone=form.cleaned_data['phone'],
        email=form.cleaned_data['email'],
        message=form.cleaned_data['message']
    )
    contact.save()

    messages.success(request, 'Contato realizado!')
    return HttpResponseRedirect("/contato/")

def show_contact_form(request):
    return render(request, 'contact_form.html', {'form': ContactForm()})

def send_contact_email(contact_data):
    subject = 'Contato eventif'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = contact_data['email']
    template_name = 'contact_email.txt'
    context = contact_data
    
    email_body = render_to_string(template_name, context)
    mail.send_mail(subject, email_body, from_email, [from_email, to_email])


def send_response_email(instance):
    subject = 'Resposta ao seu contato'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = instance.email
    
    context = {
        'name': instance.name,
        'email': instance.email,
        'phone': instance.phone,
        'message': instance.message,
        'response': instance.response,
    }

    message = render_to_string('response_email.txt', context)

    send_mail(subject, message, from_email, [to_email])

