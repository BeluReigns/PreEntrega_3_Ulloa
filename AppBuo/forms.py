from django import forms

class ComidaFormulario(forms.Form):    
    marca = forms.CharField(max_length=30)
    sabor = forms.CharField(max_length=30)
    peso = forms.IntegerField()
    precio = forms.IntegerField()
    
class JugueteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    precio = forms.IntegerField()

class RecetaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    ingrediente_estrella = forms.CharField(max_length=30)

