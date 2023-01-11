from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Pagina(models.Model):
    titulo=models.CharField(max_length=100)

    subtitulo=models.CharField(max_length=100)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo=RichTextField(blank=True, null=True)
    #cuerpo=models.TextField()
    fecha_posteo=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

"""class Imagenpost(models.Model):
        imagen=models.ImageField(null=True, blank=True, upload_to="post")
        Pagina=models.ForeignKey(Pagina, on_delete=models.CASCADE)  #IMAGEN DEL POST RELACIONADAS A LAS PAGINAS
        fecha_imagen=models.DateField(auto_now_add=True, blank=True, null=True)"""
