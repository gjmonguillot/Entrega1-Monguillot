from django.shortcuts import render
from django.http import HttpResponse

from AppProy.forms import CorredorFormulario, CarreraFormulario, IndumentariaFormulario
from AppProy.models import Corredor

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