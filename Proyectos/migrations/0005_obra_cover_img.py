# Generated by Django 3.0.5 on 2020-05-21 17:17

import Proyectos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0004_auto_20200520_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='cover_img',
            field=models.FileField(default=False, upload_to=Proyectos.models.content_file_name),
            preserve_default=False,
        ),
    ]
