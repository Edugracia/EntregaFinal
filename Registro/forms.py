from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class registrousuarioform(UserCreationForm):
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class UserEditform(UserCreationForm):
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    web_site=forms.URLField(max_length=100)
    descripcion = forms.CharField(widget=CKEditorWidget())
    avatar=forms.ImageField(label="Avatar")




    class Meta:
        model=User
        fields=["first_name", "last_name", "email", "password1", "password2", "web_site", "descripcion", "avatar"]
        help_texts = {k:"" for k in fields}


class Avatarform(forms.Form):
    imagen=forms.ImageField(label="Imagen de perfil")

