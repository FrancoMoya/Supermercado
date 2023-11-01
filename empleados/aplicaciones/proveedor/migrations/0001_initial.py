# Generated by Django 4.2.5 on 2023-10-29 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('telefono', models.PositiveIntegerField(verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('mail', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('sitio_web', models.URLField(verbose_name='Sitio Web')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('estado', models.BooleanField(verbose_name='Estado activo')),
                ('fecha', models.DateField(verbose_name='Fecha de creación')),
                ('notas', models.TextField(verbose_name='Notas')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['-fecha'],
            },
        ),
    ]
