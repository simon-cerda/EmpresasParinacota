from django.db import models
import os

def content_file_name(instance, filename):
    upload_dir = os.path.join('uploads',instance.obra.titulo)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def content_cover_name(instance, filename):
    upload_dir = os.path.join('uploads',instance.titulo)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)
# Create your models here.
class Obra(models.Model):
    fecha_ref = models.DateField()
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField()
    cliente =  models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=70)
    cover_img = models.FileField(upload_to=content_cover_name)
class Images_model(models.Model):
    img = models.FileField(upload_to=content_file_name)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)

