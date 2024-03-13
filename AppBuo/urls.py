from django.urls import path
from .views import *

urlpatterns = [

    path("", inicio),

    path('nueva_comida/', agregar_comida),
    path("buscar_comida/", buscar_comida),
    path("resultado_comida/", resultado_comida),
    path("ver_comidas/", ver_comidas),

    path('nuevo_juguete/', agregar_juguete),
    path("buscar_juguete/", buscar_juguete),
    path("resultado_juguete/", resultado_juguete),
    path("ver_juguetes/", ver_juguetes),


    path('nueva_receta/', agregar_receta),
    path("buscar_receta/", buscar_receta),
    path("resultado_receta/", resultado_receta),
    path("ver_recetas/", ver_recetas)
]