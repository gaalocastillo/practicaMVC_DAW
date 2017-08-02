from django.shortcuts import get_object_or_404, render, redirect
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
            return redirect('/')
    else:
            form=FacturaForm(instance=factura)
    return render(request, 'practica_mvc/editar_formulario.html', {'form': form})


def eliminar_factura(request,num_factura):
    
    factura  = get_object_or_404(Factura, pk = num_factura).delete()

    return HttpResponseRedirect('/')


'''
def eliminar_factura(request,num_factura):
    
    factura  = get_object_or_404(Factura, pk = num_factura).delete()
        
    return render(request, 'practica_mvc/listar_facturas.html')
'''
