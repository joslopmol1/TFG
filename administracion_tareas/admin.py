from django.contrib import admin

# Register your models here.
from .models import Sesion, Asistente, Reunion

admin.site.register(Sesion)
admin.site.register(Asistente)
admin.site.register(Reunion)
