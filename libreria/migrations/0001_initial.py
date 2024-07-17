# Generated by Django 4.1 on 2022-10-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id_pelicula', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_ingles', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('nombre_alternativo', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('imagen', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Imagen')),
                ('director', models.CharField(default='', max_length=100)),
                ('actor_1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('actor_2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('actor_3', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('actor_4', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('actor_5', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('actor_6', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('pais', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('imdb', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('resenia', models.TextField(blank=True, default='', null=True, verbose_name='Reseña')),
            ],
        ),
    ]
