# Generated by Django 5.0.2 on 2024-06-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mod_proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
