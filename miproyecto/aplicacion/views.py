from django.shortcuts import render,redirect
from .models import Pelicula,Genero
from .forms import PeliculaForm, CustomUserForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login,authenticate,logout
from social_django.models import UserSocialAuth
# Create your views here.

def salir(request):
    logout(request)
    return redirect(to='/')

def home(request):
    user=request.user
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except:
        facebook_login='nada'
    data={
        'msg':facebook_login
    }
    return render(request,'core/home.html',data)

@login_required(login_url='/login/')
def muestra_peliculas(request):
    peliculas=Pelicula.objects.all()
    data={
        'peliculas':peliculas
    }
    return render(request,'core/listado_peliculas.html',data)

@permission_required('aplicacion.add_pelicula')
def nueva_pelicula(request):
    data={
        'form':PeliculaForm
    }
    if request.POST:
        formulario=PeliculaForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Guardado Correctamente'
        data['form']=formulario

    return render(request,'core/nueva_pelicula.html',data)

def modificar_pelicula(request,id):
    pelicula=Pelicula.objects.get(id=id)
    data={
        'form':PeliculaForm(instance=pelicula)
    }
    if request.method=='POST':
        formulario=PeliculaForm(data=request.POST, instance=pelicula,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]='Modificado Correctamente'
            data['form']=PeliculaForm(instance=Pelicula.objects.get(id=id))

    return render(request,'core/modificar_pelicula.html',data)


def eliminar_pelicula(request,id):
    pelicula=Pelicula.objects.get(id=id)
    pelicula.delete()
    #redireccionar
    return redirect(to='LISTADO')

def agregar_carro(request,id):    
    peli=Pelicula.objects.get(id=id)
    if request.session.get('carro',None) is None:
        listado=PeliculasManager()
    else:
        listado=request.session.get('carro')
    
    listado.append(peli.id, peli.nombre,peli.duracion,peli.anio,peli.genero,peli.sinopsis,peli.fecha_estreno)
    request.session['carro']=listado
    return redirect(to='LISTADO')

def listado_carro(request):
    lista=request.session.get('carro')
    data={
        'listado':lista
    }
    return render(request,'core/carro.html',data)


def registro_usuario(request):
    data={
        'form':CustomUserForm()
    }
    if request.method=='POST':
        formulario=CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect(to='HOME')
    return render(request,'registration/registrar.html',data)

class PeliculaModelo(object):
    def __init__(self, id, nombre,duracion,anio,genero,sinopsis,fecha_estreno):
        self.id=id
        self.nombre=nombre
        self.duracion=duracion
        self.anio=anio
        self.genero=genero
        self.sinopsis=sinopsis
        self.fecha_estreno=fecha_estreno

    def __str__(self):
        return "%s %s %s %s %s" % (self.id, self.nombre, self.duracion, self.anio, self.genero)
 
    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)        

class PeliculasManager:
    def __init__(self):
        self.listado=[]

    def append(self, id, nombre,duracion,anio,genero,sinopsis,fecha_estreno):
        peli=PeliculaModelo(id, nombre,duracion,anio,genero,sinopsis,fecha_estreno)
        self.listado.append(peli)
    
    def search(self, key, by="id"):
        for index, book in enumerate(self.listado):
            if book.__getattribute__(by) == key:
                return index
 
    def remove(self, key, by="id"):
        index = self.search(key)
        if index != None:
            self.listado.pop(index)
            return index
 
    def __str__(self):
        s = ""
        for book in self.listado:
            s += str(book) + '\n'
        return s
