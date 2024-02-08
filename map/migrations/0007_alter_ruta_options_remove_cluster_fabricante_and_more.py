# Generated by Django 5.0 on 2024-01-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_ruta_bandeja'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ruta',
            options={'ordering': ['id'], 'verbose_name': 'Ruta', 'verbose_name_plural': 'Rutas'},
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='fabricante',
        ),
        migrations.AlterField(
            model_name='cluster',
            name='tipo',
            field=models.CharField(choices=[('mufa', 'Mufa'), ('nap', 'NAP'), ('cliente', 'Cliente')], default='horizontal', max_length=20, verbose_name='Tipo'),
        ),
    ]
