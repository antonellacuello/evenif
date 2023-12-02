from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from .views import send_response_email

@receiver(post_save, sender=Contact)
def send_response_email_on_save(sender, instance, created, **kwargs):
    # if created and instance.response:
        send_response_email(instance)
