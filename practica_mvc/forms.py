
from django import forms
from .models import Factura

import datetime

# Create your models here.
IMP_CHOICES = (
    ('0', 'pagado'),
    ('1', 'pendiente'),
    ('2', 'acumulado'),

)
class FacturaForm(forms..ModelForm):
    numero_factura = forms.CharField(max_length=16, primary_key=True)
    nombre_empresa = forms.CharField(max_length=50)
    fecha_pago = forms.DateField(initial=datetime.date.today,input_formats=['%d/%m/%Y'])
    cantidad = forms.DecimalField(min_value=0, decimal_places=2)
 
    estado = forms.ChoiceField(choices=IMP_CHOICES)

