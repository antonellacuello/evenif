from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string
from django.core import mail
from django.contrib import messages
from contact.forms import ContactForm
from django.conf import settings


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  

        if not form.is_valid():
            return render(request, 'contact_form.html', {'form': form})

        
        _send_mail(
            'Mensagem de Contato',
            settings.DEFAULT_FROM_EMAIL,
            form.cleaned_data['email'],
            'contact_email.txt',
            form.cleaned_data
        )

        messages.success(request, 'Mensagem enviada com sucesso!')
        return HttpResponseRedirect('/contact')
    else:
        form = ContactForm()
        return render(request, 'contact_form.html', {'form': form})

def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])