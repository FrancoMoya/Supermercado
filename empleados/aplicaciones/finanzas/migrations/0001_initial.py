# Generated by Django 4.2.5 on 2023-11-04 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaTransaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria Financiera',
                'verbose_name_plural': 'Categorias Financieras',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TransaccionFinanciera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.categoriatransaccion')),
            ],
            options={
                'verbose_name': 'Finanzas',
                'verbose_name_plural': 'Reportes de Finanzas',
                'ordering': ['fecha'],
            },
        ),
    ]
