from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Factura
from .forms import FacturaForm
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


def show_name(request):
	
	return render(request,'practica_mvc/prueba.html')
# def actualizar_factura(request, pk):
#     factura = get_object_or_404(Factura, pk=pk)
#     if request.method == "POST":
#         form = FacturaForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})

def listar_facturas(request):
    facturas =  Factura.objects.all()
         
    return render(request, 'practica_mvc/listar_facturas.html', {'facturas': facturas})


def crear_factura(request):
    numFactura = request.GET['numero_factura']
    nomEmpresa = request.GET['nombre_empresa']
    fechaPago = request.GET['fecha_pago']
    cant = request.GET['cantidad']

    factura = Factura(numero_factura=numFactura, nombre_empresa=nomEmpresa, fecha_pago=fechaPago, cantidad=cant)
    factura.save()

"""def actualizar_factura(request,num_factura):
    if request.method=='POST':
        try:
            factura= get_object_or_404(Factura,pk=num_factura)
        except:
            return render(request,'practica_mvc/error_page.html')

        return render(request,'practica_mvc/editar_formulario.html',{'factura':factura})
    return render(request,'practica_mvc/error_page.html')
"""
def actualizar_factura(request,num_factura):
    return render(request,'practica_mvc/error_page.html')