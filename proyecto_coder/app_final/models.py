from django.db import models

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=30)
    estilos = models.CharField(max_length=30)

class Eventos_realizados(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    fecha = models.DateField()

class Nuestros_clientes(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    