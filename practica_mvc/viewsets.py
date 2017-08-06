from .models import Factira, Recibo
from .serializers import LibroSerializer, AutorSerializer
from rest_framework import viewsets

class FacturaSerializer(viewsets.ModelViewSet):
 
    serializer_class = FacturaSerializer
    queryset = Factura.objects.all()

class ReciboSerializer(viewsets.ModelViewSet):
 
    serializer_class = ReciboSerializer
    queryset = Recibo.objects.all()