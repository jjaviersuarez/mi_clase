# Generated by Django 4.2.6 on 2023-10-18 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_alter_cursos_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=120)),
                ('apellido', models.TextField(max_length=120)),
                ('edad', models.SmallIntegerField()),
                ('fecha_creacion', models.DateField()),
                ('estado', models.SmallIntegerField()),
            ],
        ),
    ]
