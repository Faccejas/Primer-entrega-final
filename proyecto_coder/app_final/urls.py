from django.urls import path
from app_final.views import *

urlpatterns = [
    path("", Inicio, name= "inicio"),
    path("Servicios/", Servicios, name= "servicios"),
     path("Servicios/crear/", creacion_Servicios, name= "crear_servicios"),
    path("Eventos_realizados/", Eventos_realizados, name="eventos"),
    path("Nuestros_clientes/", Nuestros_clientes, name= "clientes"),
    path("Nuestros_clientes/crear/", creacion_Nuestros_clientes, name= "crear_nuevos_clientes"),
    path("Servicios/buscar/", buscar_servicio, name="buscar_servicios" ),
    path("Servicios/buscar/resultados", resultados_busqueda_servicios, name= "resultados_servicios")
]