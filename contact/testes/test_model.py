from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from contact.models import Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name='Exemplo de Contato',
            email='exemplo@email.com',
            message='Mensagem de exemplo',
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, 'Exemplo de Contato')
        self.assertEqual(self.contact.email, 'exemplo@email.com')
        self.assertEqual(self.contact.message, 'Mensagem de exemplo')
        self.assertIsNotNone(self.contact.created_at)

    def test_response_field(self):
        self.assertIsNone(self.contact.response)
