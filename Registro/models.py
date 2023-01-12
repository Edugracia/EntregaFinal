from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    #SAQUE DE ACA EL USER Y LO MANDE AL AVATAR
    nombre= models.CharField(max_length=50)
    descripcion=models.TextField()
    email=models.EmailField()
    web_site=models.URLField(max_length=100)
    instagram= models.CharField(max_length=255, null=True, blank=True)
    facebook= models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)


class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)



    """class Imagenpost(models.Model):
        imagen=models.ImageField(null=True, blank=True, upload_to="post")
        Pagina=models.ForeignKey(Pagina, on_delete=models.CASCADE)  #IMAGEN DEL POST RELACIONADAS A LAS PAGINAS
        fecha_imagen=models.DateField(auto_now_add=True, blank=True, null=True)"""

