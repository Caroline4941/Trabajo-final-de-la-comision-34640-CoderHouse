from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MensajeForm(forms.Form):
    # sender = forms.ModelChoiceField(User.objects.all())
    receiver = forms.ModelChoiceField(User.objects.all())
    mensaje = forms.CharField(max_length=5000)
    

    
    

