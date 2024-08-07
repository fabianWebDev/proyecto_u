# Generated by Django 5.0.2 on 2024-07-29 22:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sub_mod_productos', '0015_producto_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.IntegerField(default=0)),
                ('fecha_emision', models.DateField(default=datetime.date.today)),
                ('total', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FacturaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_unitario', models.FloatField(default=0.0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub_mod_facturas.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub_mod_productos.producto')),
            ],
        ),
    ]
