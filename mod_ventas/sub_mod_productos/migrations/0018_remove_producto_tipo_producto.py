# Generated by Django 5.0.2 on 2024-07-30 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_mod_productos', '0017_alter_producto_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='tipo_producto',
        ),
    ]
