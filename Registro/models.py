from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) #SAQUE DE ACA EL USER Y LO MANDE AL AVATAR DESPUES LO VUELVO A PONER PARA PROBAR LO DE LA PAG DE PERFIL
    nombre= models.CharField(max_length=50)
    descripcion=RichTextField(blank=True, null=True)
    email=models.EmailField()
    web_site=models.URLField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.nombre)


class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"




    """class Imagenpost(models.Model):
        imagen=models.ImageField(null=True, blank=True, upload_to="post")
        Pagina=models.ForeignKey(Pagina, on_delete=models.CASCADE)  #IMAGEN DEL POST RELACIONADAS A LAS PAGINAS
        fecha_imagen=models.DateField(auto_now_add=True, blank=True, null=True)"""

