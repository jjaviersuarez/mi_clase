# Generated by Django 4.2.6 on 2023-10-18 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_cursos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='nombre',
            field=models.TextField(),
        ),
    ]
