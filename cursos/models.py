from django.db import models

# Create your models here.

class Cursos(models.Model):
    #definir atributos de la entidad
    nombre = models.TextField()
    descripcion = models.TextField(max_length=300)
    aula = models.SmallIntegerField()
    #Campos de auditoria
    fecha_creacion = models.DateTimeField(auto_now=True,  null=False) 
    estado = models.SmallIntegerField(default=1)




