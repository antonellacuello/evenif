from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from contact.models import Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name='Contato',
            email='antonella@email.com',
            message='Mensagem',
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, 'Contato')
        self.assertEqual(self.contact.email, 'antonella@email.com')
        self.assertEqual(self.contact.message, 'Mensagem')
        self.assertIsNotNone(self.contact.created_at)

    def test_response_field(self):
        self.assertIsNone(self.contact.response)
