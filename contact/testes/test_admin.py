from django.test import TestCase
from django.contrib.auth.models import User
from contact.models import Contact

class ContactAdminTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin')
        self.client.login(username='admin', password='admin')
        self.contact = Contact.objects.create(
            name='contatando',
            email='antonella@email.com',
            message='mensagem',
        )

    def test_contact_model(self):
        self.assertEqual(self.contact.name, 'contatando')
        self.assertEqual(self.contact.email, 'antonella@email.com')
        self.assertEqual(self.contact.message, 'mensagem')
        self.assertIsNone(self.contact.response)  

