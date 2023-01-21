from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.urls import reverse



# Modelo de creacion de paginas (posteos)

class Pagina(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(null=True, blank=True, upload_to="post")
    cuerpo=RichTextField(null=True, blank=True)
    creado=models.DateField(auto_now_add=True)
    editado=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + " - " + str(self.user)


