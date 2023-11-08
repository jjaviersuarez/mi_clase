from django.contrib import admin
from django.urls import path, include
from cursos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('cursos/',include('cursos.urls')),
    path('accounts/',include('django.contrib.auth.urls'))
]

"""
CRUD
C: Create
R: Read
U: Update
D: Delete
"""
