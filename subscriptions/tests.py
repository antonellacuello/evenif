from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.core import mail

class SubscriptionsTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status_code 200"""
        self.assertEqual(200, self.response.status.code)

    def test_template(self):
        """Must use subscription/subscriptions_form.html"""
        self.assertTemplateUsed(self.response, 'subscription/subscriptions_form.html')

    def test_html(self):
        """HTML must contain input tags"""
        self.assertContains(self.response, "<form")
        self.assertContains(self.response, "<input", 5)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """HMTL must contain csrf"""
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context("form")
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        form = self.response.context('form')
        self.assertSequenceEqual('name', 'cpf', 'email', 'phone'), list(form.fields)

class SubscribeTestPost(TestCase):
    def setUp(self):
        data = dict(name="Antonella Cuello", 
                    cpf="12345678910", 
                    email="antonellacuello@gmail.com", 
                    phone="981451460")
        
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(302, response.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
    
    def text_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, email.subject)
    
    def test_subscription_email_sender(self):
        email = mail.outbox[0]
        expect = "contato@eventif.com.br"
        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventif.com.br', 'antonellacuello@gmail.com']
        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Antonella Cuello', email.body)
        self.assertIn('12345678910', email.body)
        self.assertIn('antonellacuello@gmail.com', email.body)
        self.assertIN('981451460', email.body)