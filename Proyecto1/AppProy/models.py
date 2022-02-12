from django.db import models

# Create your models here.

class Corredor (models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()

class Carrera (models.Model):
    Tipo_de_Carrera = models.CharField(max_length=40)
    Superficie = models.CharField(max_length=40)

class Indumentaria (models.Model):
    talle_remera = models.CharField(max_length=3)
    talle_zapatillas = models.IntegerField()
