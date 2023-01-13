from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.urls import reverse



# Modelo de creacion de paginas (posteos)

class Pagina(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo=RichTextField(blank=True, null=True)
    fecha_posteo=models.DateField(auto_now_add=True)
    actualizado=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + " - " + str(self.autor)

    def get_absolute_url(self):
        return reverse("pagina_detalle", args=(str(self.id)))



# Modelo para imagenes de paginas (posteos)

class Imagenpagina(models.Model):
    imagenpagina=models.ImageField(upload_to="post")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_posteo=models.DateField(auto_now_add=True)
    

