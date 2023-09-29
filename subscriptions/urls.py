from django.urls import path, include
from core.views import home
from subscriptions.views import subscribe
from contact.views import contact_view

app_name = 'subscriptions'

urlpatterns = [
    path('inscricao/', subscribe, name='new'),
    path('incricao/<int:pk>/', detail)
]