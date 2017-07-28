from django.shortcuts import render
from django.http import HttpResponseRedirect
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
    conn = pg.connect(dbname='practica_mvc_db',user='root',passwd='0000')
     
    consulta = 'select * from table;'
    resultado = conn.query(consulta)
    nombres  = [row[0] for row in resultado.fetchall()]
    conn.close()
     
    render(request, '.html', {'nombres': nombres})


def crear_factura(request):
    numFactura = request.GET['numero_factura']
    nomEmpresa = request.GET['nombre_empresa']
    fechaPago = request.GET['fecha_pago']
    cant = request.GET['cantidad']

    factura = Factura(numero_factura=numFactura, nombre_empresa=nomEmpresa, fecha_pago=fechaPago, cantidad=cant)
    factura.save()

def actualizar_factura(request):
    return render(request,'practica_mvc/prueba.html')
