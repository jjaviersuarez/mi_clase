# Generated by Django 4.2.6 on 2023-10-20 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_alter_cursos_nombre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Estudiantes',
        ),
        migrations.AlterField(
            model_name='cursos',
            name='fecha_creacion',
            field=models.DateTimeField(),
        ),
    ]
