from django.db import models

# Create your models here.
class Clase(models.Model):
    imagen = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    profesor = models.CharField(max_length=200)
    dia = models.CharField(max_length=200)
    hora = models.CharField(max_length=200)
    creditos = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre