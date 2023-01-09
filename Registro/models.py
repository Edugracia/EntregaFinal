from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50)
    descripcion=models.TextField()
    email=models.EmailField()
    web_site=models.URLField(max_length=100)
    instagram= models.CharField(max_length=255, null=True, blank=True)
    facebook= models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)


