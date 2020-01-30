from django.urls import path, include

from .views import *

urlpatterns = [
    path('accounts/', include('TrackerApp.auth.urls')),
    path('', index, name='index'),
]
