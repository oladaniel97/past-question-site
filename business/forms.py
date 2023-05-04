from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,label='Name',widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class': 'form-input'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-input'}))
    
    
class ContactUsForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class': 'form-inputs'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-inputs','rows':3}))
    

