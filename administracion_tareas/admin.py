from django.contrib import admin

# Register your models here.
from .models import Sesion, Asistente

admin.site.register(Sesion)
admin.site.register(Asistente)
