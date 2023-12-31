# Generated by Django 3.2.21 on 2023-10-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion_tareas', '0002_reunion'),
    ]

    operations = [
        migrations.AddField(
            model_name='sesion',
            name='asistentes',
            field=models.TextField(default='Sin asistentes'),
        ),
        migrations.AddField(
            model_name='sesion',
            name='convocatoria',
            field=models.CharField(default='Sin asistentes', max_length=200),
        ),
        migrations.AddField(
            model_name='sesion',
            name='organo_reunido',
            field=models.CharField(default='Sin órgano reunido', max_length=200),
        ),
        migrations.AddField(
            model_name='sesion',
            name='presidencia',
            field=models.CharField(default='Sin presidencia', max_length=200),
        ),
        migrations.AddField(
            model_name='sesion',
            name='tipo_sesion',
            field=models.CharField(default='Ordinaria', max_length=14),
        ),
    ]
