
from django import forms
from .models import Factura

import datetime

# Create your models here.
IMP_CHOICES = (
    ('0', 'Pagado'),
    ('1', 'Pendiente'),
    ('2', 'Acumulado'),

)
class FacturaForm(forms..ModelForm):
<<<<<<< HEAD
    numero_factura = forms.CharField(max_length=16, label="Numero de la factura")
    nombre_empresa = forms.CharField(max_length=50, label="Nombre de la empresa")
    fecha_pago = forms.DateField(initial=datetime.date.today,input_formats=['%d/%m/%Y'], label="Fecha maxima de pago")
    cantidad = forms.DecimalField(min_value=0, decimal_places=2, label="Cantidad facturada")
=======
    numero_factura = forms.CharField(max_length=16, primary_key=True)
    nombre_empresa = forms.CharField(max_length=50)
    fecha_pago = forms.DateField(initial=datetime.date.today,input_formats=['%d/%m/%Y'])
    cantidad = forms.DecimalField(min_value=0, decimal_places=2)
>>>>>>> 39dcf484a936a29321072cba72299ea9b6d20ab0
 
    estado = forms.ChoiceField(choices=IMP_CHOICES)

