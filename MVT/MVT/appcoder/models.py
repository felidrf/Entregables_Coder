from django.db import models

# Create your models here.

# CREAR ACA PARA ENTREGABLE LOS MODELOS FAMILIARES EDAD FECHA
class familiar(models.Model):
    
    nombre = models.CharField(max_length=50)
    edad = models.BigIntegerField()
    fecha = models.DateField()
    
class deporte(models.Model):

    nombre = models.CharField(max_length=50)
    cantidad_jugadores = models.IntegerField()

class equipo(models.Model):

    nombre = models.CharField(max_length=50)
    cantidad_medallas = models.IntegerField()


