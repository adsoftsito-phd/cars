from django.db import models

# Create your models here.
class Auto(models.Model):
    modelo = models.TextField(default='2003', blank = False)
    descripcion = models.TextField(default='', blank = False)
    serie = models.TextField(default='', blank = False)
    color = models.TextField(default='', blank = False)
    transmision = models.TextField(default='Manual', blank = False)
    version = models.TextField(default='standard', blank = False)
    precio = models.DecimalField(default=0, max_digits=15, decimal_places=2, blank = False)
    numero_cilindros = models.PositiveSmallIntegerField(default=4, blank = False)
    numero_puertas = models.PositiveSmallIntegerField(default=4, blank = False)
    combustible = models.TextField(default='Gasolina', blank = False)

