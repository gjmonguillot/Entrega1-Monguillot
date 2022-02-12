from django.contrib import admin
from django.urls import path
from AppProy.views import *

urlpatterns = [ 
     path('corredorformulario/', corredor_formulario, name= "CorredorFormulario"),
     path('carreraformulario/', carrera_formulario, name= "CarreraFormulario"),
     path('indumentariaformulario/', indumentaria_formulario, name= "IndumentariaFormulario"),
]
