# Generated by Django 5.0.2 on 2024-07-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_mod_productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
