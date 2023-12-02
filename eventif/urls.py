"""
URL configuration for eventif project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    
Add an import:  from my_app import views
Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    
Add an import:  from other_app.views import Home
Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    
Import the include() function: from django.urls import include, path
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core.views import home, speaker_detail
from contact.views import contact_view

urlpatterns = [
    path('', home, name= 'home'),
    path('inscricao/', include('subscriptions.urls')),
    path('palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('contato/', contact_view,name='contato'),
    path("admin/", admin.site.urls),
] 