from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from cafe.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    description=forms.CharField(label='Modificar descripcion')
    link=forms.URLField(label="Modificar link")
    imagen=forms.ImageField(label="Modificar imagen")

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name', 'description', 'link', 'imagen']
        help_texts = {k:"" for k in fields} 


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class PerfilForm(forms.Form):
    class Meta:
        model = Perfil
        fields = ['descripcion', 'link']