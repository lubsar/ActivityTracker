from django.shortcuts import render, redirect

from django.http import HttpResponse

#auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *

def index(request):
    if request.user.is_authenticated:
        #user dashboard
        return render(request, 'dashboard.html')
    else:
        #index page w/ login/register etc.
         return redirect('login')
