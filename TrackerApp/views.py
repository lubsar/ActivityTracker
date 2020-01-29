from django.shortcuts import render, HttpResponse, redirect

#auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *

def index(request):
    if request.user.is_authenticated:
        #user dashboard
        return HttpResponse("loged in")
    else:
        #index page w/ login/register etc.
         return redirect('login')
