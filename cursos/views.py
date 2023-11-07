from django.shortcuts import render
from .models import Cursos
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

#Página Index de Nuestra Aplicación
def index(request):
    return render(request,'index.html')

def inicio(request):

    db_data = Cursos.objects.all() #SELECT * FROM Cursos
    datos_cursos = {
        'cursos' : db_data,
    }
    #print(datos_cursos)
    return render(request,'inicio.html',datos_cursos)

def crear(request):
    return render(request,'crear.html')

def insertar(request):
    p_nombre = request.POST['nombre']
    p_descripcion = request.POST['descripcion']
    p_aula = request.POST['aula']
    #p_fecha_creacion = request.POST['fecha_creacion']
    #p_estado = request.POST['estado']

    db_data = Cursos(nombre = p_nombre, descripcion = p_descripcion,
                     aula = p_aula)
    #print(p_fecha_creacion)
    db_data.save() #este es el insert

    return HttpResponseRedirect(reverse(inicio))

def eliminar(request,curso_id):
    curso = Cursos.objects.filter(id=curso_id)
    curso.delete()

    return HttpResponseRedirect(reverse(inicio))

def editar(request,curso_id):
    db_data = Cursos.objects.get(pk=curso_id)
    datos_curso = {
        'curso' : db_data
    }
    return render(request,'editar.html',datos_curso)

    






