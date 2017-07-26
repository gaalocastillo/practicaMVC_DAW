from django.db import models

# Create your models here.

class Factura(models.Model):
    numero_factura = models.CharField(max_length=16)
    nombre_empresa = models.CharField(max_length=50)

