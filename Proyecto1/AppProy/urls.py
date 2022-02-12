from django.contrib import admin
from django.urls import path
from AppProy.views import *

urlpatterns = [ 
     path('corredorformulario/', corredor_formulario, name= "CorredorFormulario"),
]
