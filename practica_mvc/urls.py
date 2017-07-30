from django.conf.urls import include, url
from . import views
urlpatterns = [
        # url(r'^$', views.get_name),
        url(r'^$', views.listar_facturas,name='listar_facturas'),

        url(r'^thanks/', views.show_name),

        # url(r'^listar/', views.listar_facturas,name='listar_facturas'),
        # url(r'^facturas/lista/', views.listar_facturas),
        url(r'^facturas/edit/(?P<num_factura>\d+)/$', views.actualizar_factura,name='actualizar_factura'),

        url(r'^facturas/delete/(?P<num_factura>\d+)/$', views.eliminar_factura,name='eliminar_factura'),
        url(r'^facturas/create/$', views.crear_factura,name='crear_factura'),

    ]
