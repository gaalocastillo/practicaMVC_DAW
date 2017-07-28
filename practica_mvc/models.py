from django.db import models
import datetime

class Factura(models.Model):
    numero_factura = models.ForeignKey('auth.User')
    empresa = models.CharField(max_length=200)
    fecha_pago = models.DateField(
            default=date.today)
    cantidad = models.DecimalField(max_digits=6,decimal_places=2)
    estado = models.CharField(max_length=30)


    def guardar(self):
        self.save()

    def __str__(self):
        return self.numero_factura