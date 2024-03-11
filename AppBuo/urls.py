from django.urls import path
from .views import *

urlpatterns = [

    path('nueva_comida/', agregar_comida),
    path("buscar_comida/", buscar_comida),
    path("resultado_comida/", resultado_comida),

    path('nuevo_juguete/', agregar_juguete),
    path("buscar_juguete/", buscar_juguete),
    path("resultado_juguete/", resultado_juguete),

    path('nueva_receta/', agregar_receta),
    path("buscar_receta/", buscar_receta),
    path("resultado_receta/", resultado_receta)
    
]