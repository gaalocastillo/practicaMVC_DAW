from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from .models import Factura,Recibo
from .forms import FacturaForm,ReciboForm
import psycopg2 as pg
from .form import VoluntaryForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VoluntaryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
                   
        	 # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VoluntaryForm()

    return render(request, 'practica_mvc/voluntario.html', {'form': form})

def mostrar_principal(request):
    return render(request,'practica_mvc/index.html')



def show_name(request):
	
	return render(request,'practica_mvc/prueba.html')


def listar_facturas(request):
    facturas =  Factura.objects.all()
         
    return render(request, 'practica_mvc/listar_facturas.html', {'facturas': facturas})


def crear_factura(request):
    if request.method == 'POST':
        print ('si es post')
        form = FacturaForm(request.POST)
        if form.is_valid():
            print ('si es valid')
            factura = form.save(commit=False)
            factura.save()
            return render(request, 'practica_mvc/formulario.html', {'form': form})
        else:
            print ('no es valido')

    else:
        print ('no es post')
        form = FacturaForm()

    return render(request, 'practica_mvc/formulario.html', {'form': form})



def actualizar_factura(request, num_factura):

    factura = get_object_or_404(Factura, pk=num_factura)
    if request.method == "POST":
        form = FacturaForm(request.POST,instance=factura)
        if form.is_valid():
            factura = form.save(commit=False)
            factura.save()
            return redirect('/facturas/listar_facturas')
    else:
            form=FacturaForm(instance=factura)
    return render(request, 'practica_mvc/editar_formulario.html', {'form': form})


def eliminar_factura(request,num_factura):
    
    factura  = get_object_or_404(Factura, pk = num_factura).delete()

    return HttpResponseRedirect('/facturas/listar_facturas')



def listar_recibos(request):
    recibos =  Recibo.objects.all()
         
    return render(request, 'practica_mvc/listar_recibos.html', {'recibos': recibos})

def crear_recibo(request):
    if request.method == 'POST':
        print ('si es post')
        form = ReciboForm(request.POST)
        if form.is_valid():
            print ('si es valid')
            recibo = form.save(commit=False)
            recibo.save()
            return render(request, 'practica_mvc/crear_recibo.html', {'form': form})
        else:
            print ('no es valido')

    else:
        print ('no es post')
        form = ReciboForm()

    return render(request, 'practica_mvc/crear_recibo.html', {'form': form})



def actualizar_recibo(request, num_recibo):

    recibo = get_object_or_404(Recibo, pk=num_recibo)
    if request.method == "POST":
        form = ReciboForm(request.POST,instance=recibo)
        if form.is_valid():
            recibo = form.save(commit=False)
            recibo.save()
            return redirect('/recibos/listar_recibos')
    else:
            form=ReciboForm(instance=recibo)
    return render(request, 'practica_mvc/editar_recibo.html', {'form': form})


def eliminar_recibo(request,num_recibo):
    
    recibo  = get_object_or_404(Recibo, pk = num_recibo).delete()

    return HttpResponseRedirect('/recibos/listar_recibos')


