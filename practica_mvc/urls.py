from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.get_name),
        url(r'^thanks/', views.show_name),
        url(r'^listar/', views.listar_facturas),
        # url(r'^facturas/lista/', views.listar_facturas),
        # url(r'^facturas/(\d+)/$', views.actualizar_factura),


    ]
