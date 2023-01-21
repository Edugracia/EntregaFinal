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



    class Meta:
        model=User
        fields=["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}




class Avatarform(forms.Form):
    imagen=forms.ImageField(label="Imagen")



class ProfileEditform(forms.Form): 
    nombre=forms.CharField(label="Nombre")
    email= forms.EmailField(label="Email")
    web_site=forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=CKEditorWidget())


#MENSAJES


class MensajeForm(forms.Form):
    receptor = forms.ModelChoiceField(queryset=User.objects.all() ,label="Receptor")
    cuerpo = forms.CharField(label="Mensaje ")


