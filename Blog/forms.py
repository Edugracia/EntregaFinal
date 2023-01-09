from django import forms

class paginaform(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)

    fecha_posteo=forms.DateField()
    imagen=forms.ImageField(label="Imagen")


class Imagenform(forms.Form):
    imagen=forms.ImageField(label="Imagen")