from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import *
from django.http import HttpResponse
from mensajeria.forms import *

from django.utils.functional import SimpleLazyObject

# Create your views here.
def home(request):
    return render(request, "home.html")

def mensajeFormulario(request):
    usuario=request.user 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        formulario = MensajeForm()
        
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)

            
            paraquien = informacion['receiver']
            textoMensaje = informacion['mensaje']
            

            mensaje1 = Mensaje(enviar=(usuario), recibir = (paraquien), mensaje=textoMensaje, leido = False)
            mensaje1.save()
            return render(request, 'mensajeFormulario.html', {"form": formulario, "alerta": "mensaje enviado"} )
        else:
            return render(request, 'home.html', {"alerta": "pailas"} )
    else:
        formulario = MensajeForm()
       
    return render(request, 'mensajeFormulario.html', {"form": formulario} )

def leerMensaje(request):
    usuario = request.user
    herram = Mensaje.objects.filter(recibir = usuario)
    for mensaje in herram:
        mensaje.leido = True
        mensaje.save()
    print(herram)
    
    return render(request, "leerMensaje.html", {"mensajes": herram})

def enviadoMensaje(request):
    usuario = request.user
    herram = Mensaje.objects.filter(enviar = usuario)
    print(herram)
    
    return render(request, "enviadoMensaje.html", {"mensajes": herram})

def buscarMensaje(request):
    pass

def messages(request):
   
    if request.method == "GET":
        return render(request, 'messages.html',
                      {'users': User.objects.exclude(username=request.user.username)})