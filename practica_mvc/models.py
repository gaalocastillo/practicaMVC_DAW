from django.db import models
import datetime

class Factura(models.Model):
    numero_factura = models.CharField('Num factura', primary_key=True,max_length=16)
    empresa = models.CharField(default="-",max_length=200)
    fecha_pago = models.DateField(default=datetime.date.today)
    cantidad = models.DecimalField(default=0,max_digits=6,decimal_places=2)
    estado = models.CharField(default="acumulado",max_length=30)


    def guardar(self):
        self.save()

    def __str__(self):
        return self.numero_factura
    