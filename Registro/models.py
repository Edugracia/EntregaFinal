from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



"""class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen_perfil=models.ImageField(null=True, blank=True, upload_to="profile")
    nombre= models.CharField(max_length=50)
    cuerpo=RichTextField(blank=True, null=True)
    email=models.EmailField()
    web_site=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)"""


