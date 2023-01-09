from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    descripcion=models.TextField()
    email=models.EmailField()
    web_site=models.CharField(max_length=255, null=True, blank=True)
    #avatar=models.ImageField(null=True, blank=True, upload_to="profile")


    def __str__(self):
        return str(self.user)


class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)




