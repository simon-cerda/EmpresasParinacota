# Generated by Django 3.0.5 on 2020-05-14 00:21

import Proyectos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='img',
            field=models.FileField(upload_to=Proyectos.models.content_file_name),
        ),
    ]
