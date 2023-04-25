from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea)