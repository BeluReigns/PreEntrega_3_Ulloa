from django.db import models

# Create your models here.

class Comida(models.Model):
    
    marca = models.CharField(max_length=30)
    sabor = models.CharField(max_length=30)
    peso = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return self.marca
    

class Juguetes(models.Model):

    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
    

class Recetas(models.Model):

    nombre = models.CharField(max_length=30)
    ingrediente_estrella = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    