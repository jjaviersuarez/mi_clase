# Generated by Django 4.2.6 on 2023-10-31 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0011_alter_cursos_estado_alter_cursos_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
