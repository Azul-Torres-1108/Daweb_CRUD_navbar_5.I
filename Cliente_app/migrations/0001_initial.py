# Generated by Django 5.1 on 2024-11-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('ID_Cliente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=15)),
                ('Direccion', models.CharField(max_length=100)),
                ('Fecha_Registro', models.DateField()),
            ],
        ),
    ]
