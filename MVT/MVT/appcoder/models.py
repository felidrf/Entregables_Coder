from django.db import models

# Create your models here.

# CREAR ACA PARA ENTREGABLE LOS MODELOS FAMILIARES EDAD FECHA
class familiar(models.Model):
    
    nombre = models.CharField(max_length=50)
    edad = models.BigIntegerField()
    fecha = models.DateField()
    

