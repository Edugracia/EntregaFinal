from django import forms
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class paginaform(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)
    #autor=forms.ForeignKey(User, on_delete=models.CASCADE)
    imagen=forms.ImageField(label="Imagen")
    cuerpo=forms.CharField(widget=CKEditorWidget())