from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Pagina(models.Model):
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(null=True, blank=True, upload_to="post")
    subtitulo=models.CharField(max_length=100)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo=RichTextField(blank=True, null=True)
    #cuerpo=models.TextField()
    fecha_posteo=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

