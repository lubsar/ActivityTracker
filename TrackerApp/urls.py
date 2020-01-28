from django.urls import path, include

from .views import *

urlpatterns = [
        path('accounts/', include('django.contrib.auth.urls')),
        path('accounts/register', account_registration, name="account_registration"),
]
