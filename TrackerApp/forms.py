from django import forms

class ProjectForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, required=True)
    description = forms.CharField(label="Description", max_length=150, required=False)
