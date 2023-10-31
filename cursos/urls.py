from django.urls import path
from . import views

urlpatterns = [
    path('inicio/',views.inicio),
    path('crear/',views.crear),
    path('insertar/',views.insertar,name="insertar"),
    
]