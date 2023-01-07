from django.db import models
from django.contrib.auth.models import User
import datetime

class Producto(models.Model):
       nombre=models.CharField(max_length=50)
       precio=models.IntegerField()
       description = models.CharField(max_length=100, null=True)
       stock=models.IntegerField(null=True)
       def __str__(self):
            return self.nombre+" "+self.precio

class Marca(models.Model):
        name= models.CharField(max_length=50)
        description= models.CharField(max_length=50)
 
        def __str__(self):
            return self.name+ " " + self.description

class about(models.Model):
        description= models.CharField(max_length=50)

class Avatar(models.Model):
        imagen=models.ImageField(upload_to='avatares/', null=True, blank=True)
        user=models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.user} - {self.imagen}"

class Blog(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    cuerpo= models.TextField()
    autor= models.CharField(max_length=20)
    fecha= models.DateTimeField(default=datetime.datetime.now())
    imagen = models.ImageField(upload_to='blog/', unique=False,  null=True, blank=True)

class Perfil(models.Model):
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=100)
    link=models.URLField()
    email=models.EmailField()
    contrasena=models.CharField(max_length=25)
