from django.shortcuts import render

# Create your views here.

#Página Index de Nuestra Aplicación
def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request,'inicio.html')

