# Generated by Django 5.0.2 on 2024-07-24 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_mod_productos', '0004_alter_producto_fecha_vencimiento_alter_producto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]