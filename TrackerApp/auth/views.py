from django.shortcuts import render

#auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import *

# Create your views here.
def account_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.data['password']
            password_confirm = form.data['confirm_password']

            users = User.objects.filter(username=username)

            #username taken
            if users != None and len(users) > 0:
                return render(request, 'registration/registration.html', {'form' : form, 'user_taken' : True})
                #print('{} {} {}'.format(username, password, password_confirm))

            #passwords do not match
            if password != password_confirm:
                return render(request, 'registration/registration.html', {'form' : form, 'no_pw_match' : True})

            #save new user to database
            newuser = User.objects.create_user(username=username, password=password)
            newuser.save()

            #authenticate and log user in
            auth_user = authenticate(request, username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)

            return redirect('/')
    else:
        return render(request, 'registration/registration.html', {'form' : RegistrationForm()})

def login(request):
    pass

def logout(request):
    pass

def password_change(request):
    pass

def password_change_done(request):
    pass

def password_reset(request):
    pass
