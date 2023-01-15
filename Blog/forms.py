from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User


class paginaform(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)

    fecha_posteo=forms.DateField()
    imagen=forms.ImageField(label="Imagen")


class nuevopostform(forms.Form):
    titulo=forms.CharField(label="Titulo", max_length=100)
    subtitulo=forms.CharField(label="Subtitulo", max_length=100)    
    #imagen=forms.ImageField(label="Imagen")
    cuerpo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model=Pagina
        fields=["titulo", "subtitulo", "cuerpo"]
        help_texts = {k:"" for k in fields}

class Imagenpaginaform(forms.Form):
    imagenpagina=forms.ImageField(label="Imagen")
    
    """class Meta:
        model=Pagina
        fields=["imagenpagina"]
        help_texts = {k:"" for k in fields}""" #comente esto


class EditarPagform(forms.Form):
    titulo=forms.CharField(label="Nombre")
    subtitulo=forms.CharField(label="Apellido")
    cuerpo=forms.CharField(widget=CKEditorWidget())


    class Meta:
        model=Pagina
        fields=["titulo", "subtitulo", "cuerpo"]
        help_texts = {k:"" for k in fields}


"""class nuevopostform(forms.Form):
    titulo=forms.CharField(label="Titulo", max_length=100)
    subtitulo=forms.CharField(label="Subtitulo", max_length=100)
    #imagen=forms.ImageField(label="Imagen")
    cuerpo=forms.CharField(label="Cuerpo", widget=CKEditorWidget())

    class Meta:
        model=Pagina
        fields=["titulo", "subtitulo", "autor", "cuerpo", "fecha_posteo"]
        help_texts = {k:"" for k in fields}"""
    


