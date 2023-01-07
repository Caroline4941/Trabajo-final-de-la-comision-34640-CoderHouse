from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import  DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_protect
from register.forms import RegistroUsuarioForm
# Create your views here.

def register(request):
    if request.method== "POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, 'cafe/inicio.html', {'mensaje':f"Usuario {username} creado correctamente"})
        else:    
            return render(request, "register/register.html", {"form":form, "mensaje":"Error al crear usuario"})
    else:
        form=RegistroUsuarioForm()
    return render(request, "register/register.html", {"form":form})
