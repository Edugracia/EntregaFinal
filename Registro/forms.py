from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class registrousuarioform(UserCreationForm):
    Usuario= forms.CharField(label="Nombre de usuario")
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class UserEditform(UserCreationForm):
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")

    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class Avatarform(forms.Form):
    imagen=forms.ImageField(label="Imagen")