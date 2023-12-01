from django.urls import path

from subscriptions.views import new
from subscriptions.views import detail

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<int:pk>/', detail, name='detail'),
]