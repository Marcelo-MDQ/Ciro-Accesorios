# Generated by Django 4.1 on 2023-03-20 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0010_alter_pelicula_imagenlocal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='resenia',
            field=models.TextField(blank=True, null=True, verbose_name='Reseña'),
        ),
    ]
