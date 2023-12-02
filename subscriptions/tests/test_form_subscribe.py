from django.test import TestCase

from subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        self.form = SubscriptionForm()
        self.assertSequenceEqual(
            ['name', 'cpf', 'email', 'phone'], list(self.form.fields))

    def test_cpf_has_digit(self):
        form = self.make_validated_form(cpf='12345678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='123456')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        form = self.make_validated_form({'name': 'ANTONELLA MANUELA GONZALEZ CUELLO'})
        self.assertEqual('Antonella Manuela Gonzalez Cuello', form.cleaned_data['name'])

    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
form = self.make_validated_form({'phone': ''})
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['all'], list(form.errors))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        error_list = errors[field]
        exception = error_list[0]
        self.assertEqual(code, exception.code)


    def assertFormErrorMessage (self, form, field, msg):
        errors = form.errors
        error_list = errors[field]
        self.assertListEqual([msg], error_list)


    def make_validated_form(self, kwargs):
        valid = dict(name="Antonella Cuello",
                    cpf="12345678901",
                    email="antonella.cuello@aluno.riogrande.ifrs.edu.br",
                    phone="53981451460")
        data = dict(valid, kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form 