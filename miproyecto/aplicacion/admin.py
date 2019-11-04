from django.contrib import admin
from .models import Genero,Pelicula
# Register your models here.

class PeliculaAdmin(admin.ModelAdmin):
    list_display=['nombre', 'duracion','anio','genero']
    search_fields=['nombre', 'anio']
    list_filter=['genero']
    list_per_page=1


admin.site.register(Genero)
admin.site.register(Pelicula,PeliculaAdmin)
