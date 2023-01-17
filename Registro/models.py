from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Profile(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE) #SAQUE DE ACA EL USER Y LO MANDE AL AVATAR DESPUES LO VUELVO A PONER PARA PROBAR LO DE LA PAG DE PERFIL
    nombre= models.CharField(max_length=50)
    descripcion=RichTextField(blank=True, null=True)
    email=models.EmailField()
    web_site=models.URLField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.user} - {self.nombre} - {self.pk}"


class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"


#MENSAJERIA

"""class Mensajesalida(models.Model):
    emisor=models.ForeignKey(User, on_delete=models.CASCADE)#sacarlo de la form
    receptor=models.ForeignKey(Profile.user, on_delete=models.CASCADE)
    cuerpo=models.TextField(max_length=250, blank=True, null=True)
    enviado=models.DateField(auto_now_add=True)
    #leido=models.BooleanField()

    def __str___(self):
        return f"{self.emisor}"

class Mensajeentrada(models.Model):
    receptor=models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo=models.TextField(max_length=250, blank=True, null=True)
    enviado=models.DateField(auto_now_add=True)
    #leido=models.BooleanField()

    def __str___(self):
        return f"{self.receptor}"


class mensaje(models.Model):
    mensaje= models.ManyToManyField(Mensajesalida),
    emisor= models.ForeignKey(Emisor, on_delete=models.CASCADE)
    receptor= models.ForeignKey(Receptor, on_delete=models.CASCADE)



    class Imagenpost(models.Model):
        imagen=models.ImageField(null=True, blank=True, upload_to="post")
        Pagina=models.ForeignKey(Pagina, on_delete=models.CASCADE)  #IMAGEN DEL POST RELACIONADAS A LAS PAGINAS
        fecha_imagen=models.DateField(auto_now_add=True, blank=True, null=True)

class Emisor(models.Model):
    emisor=models.ForeignKey(User, on_delete=models.CASCADE)
    #receptor=models.ForeignKey(Profile.user, on_delete=models.CASCADE)
    cuerpo=models.TextField(max_length=250, blank=True, null=True)
    enviado=models.DateField(auto_now_add=True)
    #leido=models.BooleanField()

    def __str___(self):
        return f"{self.emisor}"

class Receptor(models.Model):
    receptor=models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo=models.TextField(max_length=250, blank=True, null=True)
    recibido=models.DateField(auto_now_add=True)
    #leido=models.BooleanField()

    def __str___(self):
        return f"{self.receptor}"""