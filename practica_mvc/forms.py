
from django import forms
from .models import Factura
from .models import Recibo
from .models import Ticket

import datetime

# Create your models here.
IMP_CHOICES = (
    ('Pagado', 'Pagado'),
    ('Pendiente', 'Pendiente'),
    ('Acumulado', 'Acumulado'),

)



class FacturaForm(forms.ModelForm):
	class Meta:
		model = Factura
		fields = ('numero_factura', 'empresa', 'fecha_pago', 'cantidad', 'estado')

class ReciboForm(forms.ModelForm):
	class Meta:
		model = Recibo
		fields = ('numero_recibo', 'fecha_pago', 'nombre', 'concepto', 'cantidad')
		
class TicketForm(forms.ModelForm):	
	class Meta:
		model = Ticket
		fields = ('origen', 'destino', 'precio', 'adquiriente','puesto')

class LoginForm(forms.Form):
	name=forms.CharField(max_length=10)
	password= forms.CharField(widget=forms.PasswordInput)
class ValorForm(forms.form):
	valor1=forms.CharField(max_length=10)
	valor2=forms.CharField(max_length=10)
	'''
	numero_factura = forms.CharField(max_length=16, label="Numero de la factura")
	nombre_empresa = forms.CharField(max_length=50, label="Nombre de la empresa")
	fecha_pago = forms.DateField(initial=datetime.date.today,input_formats=['%d/%m/%Y'], label="Fecha maxima de pago")
	cantidad = forms.DecimalField(min_value=0, decimal_places=2, label="Cantidad facturada")
	estado = forms.ChoiceField(choices=IMP_CHOICES)
	'''
