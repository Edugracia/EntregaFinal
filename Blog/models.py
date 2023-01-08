from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
class Pagina(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo=models.TextField()
    fecha_posteo=models.DateField(auto_now_add=True)
    imagen=models.ImageField(upload_to="post", null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

