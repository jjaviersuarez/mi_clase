from django.shortcuts import render
from .models import Cursos

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
    p_fecha_creacion = request.POST['fecha_creacion']
    p_estado = request.POST['estado']

    db_data = Cursos(nombre = p_nombre, descripcion = p_descripcion,
                     aula = p_aula, fecha_creacion = p_fecha_creacion,
                     estado = p_estado)
    print(p_fecha_creacion)
    db_data.save() #este es el insert

    db_data = Cursos.objects.all() #SELECT * FROM Cursos
    datos_cursos = {
        'cursos' : db_data,
    }
    return render(request,'inicio.html',datos_cursos)
    






