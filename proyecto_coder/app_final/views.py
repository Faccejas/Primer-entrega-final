from django.shortcuts import render
from django.http import HttpResponse
from app_final.models import *
from app_final.forms import *

# Create your views here.

def Inicio (request):
    return render(request, "app_final/index.html")


def Servicios (request):
    return render(request, "app_final/servicios.html")


def creacion_Servicios (request):
    if request.method == "POST":
        nombre_servicio = request.POST["nombre"]
        nombre_estilos = request.POST["estilos"]

        servicio = Servicios(nombre = nombre_servicio, estilos = nombre_estilos)
        servicio.save()
        
    return render(request, "app_final/servicio_formulario.html")




def Eventos_realizados (request):
    return render(request, "app_final/eventos_realizados.html")





def Nuestros_clientes (request):
    return render(request, "app_final/nuestros_clientes.html")


def creacion_Nuestros_clientes (request):
    
    if request.method == "POST":
        formulario = NuestrosclientesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nuestros_clientes = Nuestros_clientes(nombre = data["nombre"], categoria = data["categoria"])
            nuestros_clientes.save()
        return render(request, "app_final/index.html")
        
    else:
        formulario = NuestrosclientesFormulario()
    contexto = {"formulario": formulario}
    return render(request, "app_final/nuestros_clientes_formulario.html", contexto)






def resultados_busqueda_servicios(request):
    print(request.GET)
    return render(request, "app_final/resultados_busqueda_servicios.html")
    

def buscar_servicio (request):

    return render(request, "app_final/busqueda_servicios.html")