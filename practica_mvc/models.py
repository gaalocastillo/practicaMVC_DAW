from django.db import models
import datetime

IMP_CHOICES = (
    ('Pagado', 'Pagado'),
    ('Pendiente', 'Pendiente'),
    ('Acumulado', 'Acumulado'),

)
class Factura(models.Model):
    numero_factura = models.CharField('Num factura', primary_key=True,max_length=16)
    empresa = models.CharField(default="-",max_length=200)
    fecha_pago = models.DateField(default=datetime.date.today)
    #fecha_pago = models.CharField(default="-",max_length=200)

    cantidad = models.DecimalField(default=0,max_digits=6,decimal_places=2)
    estado = models.CharField(default="acumulado",max_length=25,choices=IMP_CHOICES)


    def save(self,*args, **kwargs):
        super(Factura,self).save(*args, **kwargs)

    def __str__(self):
        return self.numero_factura


class Recibo(models.Model):
    numero_recibo = models.CharField('nun recibo', primary_key=True,max_length=16)
    fecha_pago = models.DateField(default=datetime.date.today)
    nombre = models.CharField(default=" ",max_length=200)
    concepto = models.CharField(default=" ",max_length=200)
    cantidad = models.DecimalField(default=0,max_digits=6,decimal_places=2)
    

    def save(self,*args, **kwargs):
        super(Recibo,self).save(*args, **kwargs)

    def __str__(self):
        return self.numero_recibo
    