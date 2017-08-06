from .models import Factura, Recibo
from .serializers import FacturaSerializer, ReciboSerializer
from rest_framework import viewsets

class FacturaViewSet(viewsets.ModelViewSet):
 
    serializer_class = FacturaSerializer
    queryset = Factura.objects.all()

class ReciboViewSet(viewsets.ModelViewSet):
 
    serializer_class = ReciboSerializer
    queryset = Recibo.objects.all()