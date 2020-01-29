from django.urls import path, include

from .views import *

urlpatterns = [
        path('', include('django.contrib.auth.urls')),
        path('register', account_registration, name="account_registration"),
]
