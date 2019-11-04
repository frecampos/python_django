from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.
class Genero(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    nombre=models.CharField(max_length=30)
    duracion=models.IntegerField()
    anio=models.IntegerField(verbose_name='Año')
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
    sinopsis =models.TextField(null=True,blank=True)
    fecha_estreno=models.DateField()
    imagen=models.ImageField(upload_to="img",null=True,blank=True)

    def __str__(self):
        return self.nombre

    class Meta:

        permissions=(
            ('is_usuario', _('Is Usuario')),
            ('is_admin', _('Is Admin')),
        )