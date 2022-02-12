from django.shortcuts import render
from django.http import HttpResponse

from AppProy.forms import CorredorFormulario, CarreraFormulario, IndumentariaFormulario
from AppProy.models import Corredor, Carrera, Indumentaria

# Create your views here.

def corredor_formulario(request):
    if request.method == 'POST':
        miFormulario = CorredorFormulario(request.POST) #Aquí me llega toda la info del html
        print(miFormulario)
        
        if miFormulario.is_valid:     #Si pasa la validación de Django 
            informacion = miFormulario.data     #el nombre no importa
            
            r_nombre = informacion['nombre']
            r_apellido = informacion['apellido']
            r_edad = informacion['edad']
            r_email = informacion['email']
        
            corredor = Corredor(nombre=r_nombre, apellido=r_apellido, edad=r_edad, email=r_email)
            corredor.save()
    
    miFormulario = CorredorFormulario() #formulario vacio
    return render(request, 'AppProy/corredorformulario.html', {"miFormulario": miFormulario})



def carrera_formulario(request):
    if request.method == 'POST':
        miFormulario2 = CarreraFormulario(request.POST) #Aquí me llega toda la info del html
        print(miFormulario2)
        
        if miFormulario2.is_valid:     #Si pasa la validación de Django 
            informacion2 = miFormulario2.data     #el nombre no importa
            
            r_tipo_carrera = informacion2['Tipo_de_Carrera']
            r_superficie = informacion2['Superficie']
        
            carrera = Carrera(Tipo_de_Carrera=r_tipo_carrera, Superficie=r_superficie)
            carrera.save()

    miFormulario2 = CarreraFormulario() #formulario vacio
    return render(request, 'AppProy/carreraformulario.html', {"miFormulario2": miFormulario2})


def indumentaria_formulario(request):
    if request.method == 'POST':
        miFormulario3 = IndumentariaFormulario(request.POST) #Aquí me llega toda la info del html
        print(miFormulario3)
        
        if miFormulario3.is_valid:     #Si pasa la validación de Django 
            informacion3 = miFormulario3.data     #el nombre no importa
            
            r_talle_remera = informacion3['talle_remera']
            r_talle_zapatillas = informacion3['talle_zapatillas']
        
            talles = Indumentaria(talle_remera=r_talle_remera, talle_zapatillas=r_talle_zapatillas)
            talles.save()

    miFormulario3 = IndumentariaFormulario() #formulario vacio
    return render(request, 'AppProy/indumentariaformulario.html', {"miFormulario3": miFormulario3})



def busquedaCorredor(request):
    return render(request, "AppProy/busquedacorredor.html")


def buscar(request):
    respuesta = f"Estoy buscando al Corredor: {request.GET['nombre'] }" 
    return HttpResponse(respuesta)


