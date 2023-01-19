from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

from .models import Mensaje

class registrousuarioform(UserCreationForm):
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}



class UserEditform(UserCreationForm): #PROFILE EDIT FORM?????? la profile que trae de la page list es la data del profile pero de la que se carga en la form
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    web_site=forms.URLField(max_length=100)
    descripcion = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model=User
        fields=["first_name", "last_name", "email", "password1", "password2", "web_site", "descripcion"]
        help_texts = {k:"" for k in fields}


"""class UserEditform(UserCreationForm): #PROFILE EDIT FORM?????? la profile que trae de la page list es la data del profile pero de la que se carga en la form
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    web_site=forms.URLField(max_length=100)
    descripcion = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model=User
        fields=["first_name", "last_name", "email", "password1", "password2", "web_site", "descripcion"]
        help_texts = {k:"" for k in fields}"""



class Avatarform(forms.Form):
    imagen=forms.ImageField(label="Imagen")


#SUBI IMAGEN DE PERFIL Y ESTOY TRATANDO DE MANDARLA A LA FORM




#MENSAJES

class Mensajeform(forms.Form):
    #receptor=forms.CharField() #ESTE SERIA EL USERNAME
    cuerpo=forms.CharField(label="Tu mensaje")
    
    

    class Meta:
        model=Mensaje #y si esto en vez de user es de mensaje?
        fields=["receptor", "cuerpo"]
        help_texts = {k:"" for k in fields}



"""class Mensajesalidaform(forms.Form):
    #receptor=forms.CharField(label="#") #ver de que manera 
    cuerpo=forms.CharField(label="Tu mensaje")
    
    

    class Meta:
        model=User
        fields=["receptor", "cuerpo"]
        help_texts = {k:"" for k in fields}"""


