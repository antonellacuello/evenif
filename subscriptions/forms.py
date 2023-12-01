from django import forms 
from subscriptions.models import Subscription
from subscriptions.validators import validate_cpf
from django.core.exceptions import ValidationError

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']


    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()
        if (not self.cleaned_data['email'] and \
            not self.cleaned_data['phone']):
            raise ValidationError('Informe seu email ou telefone')