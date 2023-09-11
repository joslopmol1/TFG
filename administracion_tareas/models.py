from django.db import models

# Create your models here.

class Sesion(models.Model):
    numero_sesion = models.IntegerField(unique=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_finalizacion = models.TimeField()
    lugar = models.CharField(max_length=200)
    temas_tratados = models.TextField()
    acuerdos_adoptados = models.TextField()

    def __str__(self):
        return f"Sesión {self.numero_sesion}"

class Asistente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre