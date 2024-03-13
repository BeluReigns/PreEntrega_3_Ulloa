from django.shortcuts import render
from AppBuo.models import *
from .forms import ComidaFormulario, JugueteFormulario, RecetaFormulario

# Create your views here.

def inicio(request):

    return render(request, "inicio.html")

# Vistas para formularios
def agregar_comida(request):
    
    # Si le he dado click al botón enviar
    if request.method == "POST":

      # Formulario es un objeto de la clase ComidaFormulario
        formulario = ComidaFormulario(request.POST) 

        if formulario.is_valid():
            info_dict = formulario.cleaned_data            
            nueva_comida = Comida(marca = info_dict["marca"],
                                  sabor = info_dict["sabor"],
                                  peso = info_dict["peso"],
                                  precio = info_dict["precio"])
            
            nueva_comida.save()

            return render(request, "inicio.html")
        
    else:

        formulario = ComidaFormulario()
        
    return render(request, "nueva_comida.html", {"form":formulario})


def agregar_juguete(request):
    
    if request.method == "POST":

        formulario = JugueteFormulario(request.POST) 

        if formulario.is_valid():

            info_dict = formulario.cleaned_data
            
            nuevo_juguete = Juguetes(nombre = info_dict["nombre"],
                                     descripcion = info_dict["descripcion"],
                                     precio = info_dict["precio"])
            
            nuevo_juguete.save()

            return render(request, "inicio.html")
        
    else:

        formulario = JugueteFormulario()
        
    return render(request, "nuevo_juguete.html", {"form":formulario})


def agregar_receta(request):
    
    if request.method == "POST":

        formulario = RecetaFormulario(request.POST) 

        if formulario.is_valid():

            info_dict = formulario.cleaned_data
            
            nueva_receta = Recetas(nombre = info_dict["nombre"],
                                   ingrediente_estrella = info_dict["ingrediente_estrella"])
            
            nueva_receta.save()
        
            return render(request, "inicio.html")

    else:

        formulario = RecetaFormulario()
        
    return render(request, "nueva_receta.html", {"form":formulario})


# Buscar y mostrar resultados de la búsqueda

# Vista para mostrar el formulario de búsqueda
def buscar_comida(request):
    
    return render(request, "buscar_comida.html")

def buscar_juguete(request):
    
    return render(request, "buscar_juguete.html")

def buscar_receta(request):
    
    return render(request, "buscar_receta.html")

# Vista para mostrar los resultados de la búsqueda
def resultado_comida(request):

    comida = request.GET["comida"] # Esta palabra debe ser la misma de name= en el html   
    
    resultados = Comida.objects.filter(marca__iexact=comida)    

    return render(request, "resultado_comida.html", {"resultado":resultados})

def resultado_juguete(request):

    juguete = request.GET["juguete"]    
    
    resultados = Juguetes.objects.filter(nombre__iexact=juguete)    

    return render(request, "resultado_juguete.html", {"resultado1":resultados})

def resultado_receta(request):

    receta = request.GET["receta"]    
    
    resultados = Recetas.objects.filter(nombre__iexact=receta)    

    return render(request, "resultado_receta.html", {"resultado2":resultados})

def ver_comidas(request):
    return render(request, "ver_comidas.html")

def ver_juguetes(request):
    return render(request, "ver_juguetes.html")

def ver_recetas(request):
    return render(request, "ver_recetas.html")