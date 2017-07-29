from django.db import models
import datetime

IMP_CHOICES = (
    ('0', 'Pagado'),
    ('1', 'Pendiente'),
    ('2', 'Acumulado'),

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
    