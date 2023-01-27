from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User



class nuevopostform(forms.Form):
    titulo=forms.CharField(label="Titulo", max_length=100)
    subtitulo=forms.CharField(label="Subtitulo", max_length=100)    
    imagen=forms.ImageField()
    cuerpo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model=Pagina
        fields=["titulo", "subtitulo", "imagen", "cuerpo"]
        help_texts = {k:"" for k in fields}



class EditarPagform(forms.Form):
    titulo=forms.CharField(label="Titulo")
    subtitulo=forms.CharField(label="Subtitulo")
    imagen=forms.ImageField()
    cuerpo=forms.CharField(widget=CKEditorWidget())


    class Meta:
        model=Pagina
        fields=["titulo", "subtitulo", "imagen", "cuerpo"]
        help_texts = {k:"" for k in fields}


class Imagenpaginaform(forms.Form):
    imagenpagina=forms.ImageField(label="Imagen")


