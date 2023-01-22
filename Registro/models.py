from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"


#MENSAJERIA

class Mensaje(models.Model):
    emisor=models.ForeignKey(User, related_name= "emisor", on_delete=models.CASCADE)
    receptor=models.ForeignKey(User, related_name= "receptor", on_delete=models.CASCADE)
    cuerpo=models.TextField(max_length=250, blank=True, null=True)
    enviado=models.DateField(auto_now_add=True)
    #leido=models.BooleanField()

    def __str___(self):
        return f"{self.emisor} - {self.receptor}"
