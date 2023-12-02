from django.test import TestCase
from django.urls import reverse
from django.core import mail
from contact.forms import ContactForm

class ContactViewTestes(TestCase):
    def test_get_contact_page(self):
        response = self.client.get(reverse('contato'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_form.html')

    def test_valid_post_contact_form(self):
        form_data = {
            'name': 'Antonella Cuello',
            'phone': '53981451460',
            'email': 'antonella.cuello@aluno.riogrande.ifrs.edu.br',
            'message': 'HAHAHAHAHAHHAHAHAHAHAHA'
        }
        response = self.client.post(reverse('contato'), data=form_data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(len(mail.outbox), 1)  

    def test_invalid_post_contact_form(self):
        form_data = {}  
        response = self.client.post(reverse('contato'), data=form_data)
        self.assertEqual(response.status_code, 200)  
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_send_email(self):
        mail.send_mail(
            'Mensagem de Contato',
            'Mensagem Teste',
            'antonella.cuello@aluno.riogrande.ifrs.edu.br',
            ['contato@eventif.com.br']
        )
        self.assertEqual(len(mail.outbox), 1)  
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.subject, 'Mensagem de Contato')
        self.assertEqual(sent_email.from_email, 'antonella.cuello@aluno.riogrande.ifrs.edu.br')
        self.assertEqual(sent_email.to, ['contato@eventif.com.br'])