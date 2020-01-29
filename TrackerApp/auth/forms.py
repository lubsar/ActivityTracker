from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=30)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password", max_length=30)
