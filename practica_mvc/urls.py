
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from . import views

from .viewsets import FacturaViewSet, ReciboViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'facturas', FacturaViewSet)
router.register(r'recibos', ReciboViewSet)


urlpatterns = [
        # url(r'^$', views.get_name),
        url(r'^$', views.mostrar_principal,name='mostrar_principal'),

        url(r'^thanks/', views.show_name),

        # url(r'^listar/', views.listar_facturas,name='listar_facturas'),
        # url(r'^facturas/lista/', views.listar_facturas),
        url(r'^facturas/listar_facturas', views.listar_facturas,name='listar_facturas'),
        url(r'^facturas/edit/(?P<num_factura>\d+)/$', views.actualizar_factura,name='actualizar_factura'),
        url(r'^facturas/delete/(?P<num_factura>\d+)/$', views.eliminar_factura,name='eliminar_factura'),
        url(r'^facturas/create/$', views.crear_factura,name='crear_factura'),


        url(r'^recibos/listar_recibos', views.listar_recibos,name='listar_recibos'),
        url(r'^recibos/edit/(?P<num_recibo>\d+)/$', views.actualizar_recibo,name='actualizar_recibo'),
        url(r'^recibos/delete/(?P<num_recibo>\d+)/$', views.eliminar_recibo,name='eliminar_recibo'),
        url(r'^recibos/create/$', views.crear_recibo,name='crear_recibo'),
        url(r'^', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    ]