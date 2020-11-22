from django.db import models
from clases.models import Clase

# Create your models here.
class Estudiante(models.Model):
    imagen = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    paterno = models.CharField(max_length=200)
    materno = models.CharField(max_length=200)
    estatus = models.CharField(max_length=200)
    carrera = models.CharField(max_length=200)
    creditos = models.CharField(max_length=200) 
    clase = models.ManyToManyField(Clase, related_name='clase')
