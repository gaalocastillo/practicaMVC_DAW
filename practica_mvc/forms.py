
from django import forms
from .models import Factura
import datetime

# Create your models here.
IMP_CHOICES = (
    ('Pagado', 'Pagado'),
    ('Pendiente', 'Pendiente'),
    ('Acumulado', 'Acumulado'),

)

<<<<<<< HEAD
class FacturaForm(forms.ModeñForm):


=======
<<<<<<< HEAD
class FacturaForm(forms.ModelForm):
	class Meta:
		model = Factura
		fields = ('numero_factura', 'empresa', 'fecha_pago', 'cantidad', 'estado')
=======
class FacturaForm(forms.Form):
>>>>>>> da100581b6f0f94582be88878d63cc684e7c979c
>>>>>>> 7506958d0041514cf8f2fd7de0b5834da7097673

	'''
	numero_factura = forms.CharField(max_length=16, label="Numero de la factura")
	nombre_empresa = forms.CharField(max_length=50, label="Nombre de la empresa")
	fecha_pago = forms.DateField(initial=datetime.date.today,input_formats=['%d/%m/%Y'], label="Fecha maxima de pago")
	cantidad = forms.DecimalField(min_value=0, decimal_places=2, label="Cantidad facturada")
	estado = forms.ChoiceField(choices=IMP_CHOICES)
	'''