# Generated by Django 5.0.2 on 2024-07-24 01:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_mod_productos', '0005_alter_producto_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
