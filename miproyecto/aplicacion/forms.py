from django import forms
from django.forms import ModelForm
from .models import Pelicula
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeliculaForm(ModelForm):
    nombre=forms.CharField(max_length=200,min_length=2)
    duracion=forms.IntegerField(min_value=5,max_value=500)

    class Meta:
        model= Pelicula
        fields=['nombre','duracion','anio','genero','sinopsis','fecha_estreno','imagen']
        widgets={
            'fecha_estreno':forms.SelectDateWidget(years=range(1920,2020))
        }

    def clean_fecha_estreno(self):
        fecha=self.cleaned_data['fecha_estreno']
        if fecha> datetime.date.today():
            raise forms.ValidationError('la fecha no pueded ser mayor al dia de hoy ')
        return fecha

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
