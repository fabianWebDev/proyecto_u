# Generated by Django 5.0.2 on 2024-06-09 06:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
