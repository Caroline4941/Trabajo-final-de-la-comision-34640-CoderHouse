from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import  DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'cafe/inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'login/login.html', {'mensaje': "Usuario o contraseña incorrectos", 'form':form})
        else:
            return render(request, 'login/login.html', {'mensaje': "Usuario o contraseña incorrectos", 'form':form})
    else:
        form = AuthenticationForm()
    return render(request,"login/login.html", {"form":form})            