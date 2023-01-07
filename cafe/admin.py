from django.contrib import admin
from .models import *
from mensajeria.models import *

# Register your models here.

admin.site.register(Avatar)
admin.site.register(Mensaje)
admin.site.register(Blog)

