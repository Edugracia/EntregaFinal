from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class paginaform(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)

    fecha_posteo=forms.DateField()
    imagen=forms.ImageField(label="Imagen")


class nuevopostform(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)
    #imagen=forms.ImageField(label="Imagen")
    cuerpo=forms.CharField(widget=CKEditorWidget())

    class Meta:
        model=Pagina
        fields=["titulo", "subtitulo", "autor", "cuerpo", "fecha_posteo"]
        help_texts = {k:"" for k in fields}
    


