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

    send_contact_email(form.cleaned_data)

    messages.success(request, 'Contato realizado!')
    return redirect('contato_sucesso')  # Supondo que você tenha uma página de sucesso chamada 'contato_sucesso'

    messages.success(request, 'Contato realizado!')
    return HttpResponseRedirect("/contact/")

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


