# Generated by Django 5.0.2 on 2024-08-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_mod_productos', '0019_producto_tipo_producto_tipoproducto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default='productos/default.png', null=True, upload_to='productos/'),
        ),
    ]