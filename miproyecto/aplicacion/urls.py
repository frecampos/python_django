from django.contrib import admin
from django.urls import path,include
from .views import agregar_carro,home,muestra_peliculas, nueva_pelicula,modificar_pelicula,eliminar_pelicula,registro_usuario,salir,listado_carro
from django.conf.urls import url

urlpatterns = [
    path('', home,name='HOME'),
    path('home/', home,name='HOME'),
    path('listado_peliculas/',muestra_peliculas,name='LISTADO'),
    path('nueva_pelicula/',nueva_pelicula,name='NUEVAPELICULA'),
    path('modificar_pelicula/<id>/',modificar_pelicula,name='MODIFICARPELICULA'),
    path('eliminar_pelicula/<id>/',eliminar_pelicula,name='ELIMINARPELICULA'),
    path('registro/',registro_usuario,name='REGISTRO'),
    path('salir/',salir,name='SALIR'),
    url('',include('social.apps.django_app.urls',namespace='social')),
    path('listado_carro/',listado_carro,name='LISTADOCARRO'),
    path('agregar_carro/<id>/',agregar_carro,name='AGREGARCARRO'),
]