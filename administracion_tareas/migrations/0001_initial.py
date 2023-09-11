# Generated by Django 4.2.4 on 2023-09-01 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_sesion', models.IntegerField(unique=True)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_finalizacion', models.TimeField()),
                ('lugar', models.CharField(max_length=200)),
                ('temas_tratados', models.TextField()),
                ('acuerdos_adoptados', models.TextField()),
            ],
        ),
    ]