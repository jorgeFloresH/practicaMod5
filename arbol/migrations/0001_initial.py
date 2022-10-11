# Generated by Django 4.1.2 on 2022-10-10 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=100)),
                ('nro', models.CharField(max_length=100)),
                ('zona', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latidud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('distrito', models.IntegerField(default=0)),
                ('subdistrito', models.IntegerField(default=0)),
                ('codigoCatastral', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tipoArbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Arbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('codigoArbol', models.CharField(max_length=100, unique=True)),
                ('direccionArbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbol.direccion')),
                ('fotoArbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbol.foto')),
                ('predioArbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbol.predio')),
                ('tipoArbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbol.tipoarbol')),
            ],
        ),
    ]