from django import forms

# Create your models here.

class CorredorFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    edad = forms.IntegerField()
    email = forms.EmailField()

class CarreraFormulario (forms.Form):
    Tipo_de_Carrera = forms.CharField(max_length=40)
    Superficie = forms.CharField(max_length=40)

class IndumentariaFormulario (forms.Form):
    talle_remera = forms.CharField(max_length=3)
    talle_zapatillas = forms.IntegerField()