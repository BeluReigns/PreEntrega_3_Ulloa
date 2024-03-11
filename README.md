# PreEntrega_3
### Django
- La versión utilizada en este programa es la: 5.0.2
- Si tiene una anterior, instalar o actualizar Django a versión necesaria Linux/Mac: `python -m pip install Django==5.0.3`  Windows: `py -m pip install Django==5.0.3`

### Con el proyecto abierto en VSC u otro:
1. Hacer el paso previo para poder hacer la migración: `python manage.py makemigrations`
2. Luego hacer la migración: `python manage.py migrate`
Una vez tengamos las migraciones podemos correr el servidor: `python manage.py runserver`
Con el servidor corriendo podemos hacer uso/pruebas del programa de forma local.

### URLs de uso local 
- http://127.0.0.1:8000/AppBuo/
  #### Comida
  - http://127.0.0.1:8000/AppBuo/nueva_comida/
  - http://127.0.0.1:8000/AppBuo/buscar_comida/ -> Buscar puppy o proplan o brit
  - Que te llevará a "LocalHost/AppBuo/resultado_comida/?comida=puppy" al hacer la búsqueda

  #### Juguetes
  - http://127.0.0.1:8000/AppBuo/nuevo_juguete/
  - http://127.0.0.1:8000/AppBuo/buscar_juguete/ -> Buscar pelota o hueso o piscina
  - Que te llevará a "LocalHost/AppBuo/resultado_juguete/?juguete=pelota" al hacer la búsqueda

  #### Recetas
  - http://127.0.0.1:8000/AppBuo/nueva_receta/
  - http://127.0.0.1:8000/AppBuo/buscar_receta/ -> Buscar helados o calugas o galleta de avena
  - Que te llevará a "LocalHost/AppBuo/resultado_receta/?receta=helados" al hacer la búsqueda

- Una vez hechas todas las pruebas se puede cerrar el servidor con `Ctrl + c`


