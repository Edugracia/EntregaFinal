from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class paginaform(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)

    fecha_posteo=forms.DateField()
    imagen=forms.ImageField(label="Imagen")