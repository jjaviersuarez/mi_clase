from django.urls import path
from . import views

urlpatterns = [
    path('inicio/',views.inicio,name="cursos"),
    path('crear/',views.crear,name="crear"),
    path('insertar/',views.insertar,name="insertar"),
    path('eliminar/<int:curso_id>',views.eliminar,name="eliminar"),
    path('editar/<int:curso_id>',views.editar,name="editar"),
    path('actualizar/',views.actualizar,name="actualizar"),
    path('logout/',views.exit,name="exit")
]