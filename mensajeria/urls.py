from django.urls import path, include
from django.contrib import admin
from django.urls import path
from mensajeria.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("mensajeFormulario", mensajeFormulario , name = "mensajeFormulario"),
    path("messages", messages , name = "messages"),
    path("leerMensaje", leerMensaje , name = "leerMensaje"),
    path("enviadoMensaje", enviadoMensaje , name = "enviadoMensaje"),
]