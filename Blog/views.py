from django.shortcuts import render
from .models import *
from Blog.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def inicio(request):
    return render (request, "inicio.html")

def blogs(request):
    return render (request, "blogs.html")

#Vistas de paginas

class PaginaCreacion(LoginRequiredMixin,CreateView):
    model = Pagina
    template_name="pagina_form.html", 
    success_url = reverse_lazy('pagina_lista')
    fields=['titulo', 'subtitulo', 'autor', 'cuerpo', 'imagen']



"""class PaginaCreacion(LoginRequiredMixin,CreateView):
    model = Pagina
    template_name="pagina_form.html"
    success_url = reverse_lazy('pagina_lista')
    fields=['titulo', 'subtitulo', 'autor', 'cuerpo', 'imagen']"""

class PaginaUpdate(LoginRequiredMixin,UpdateView):
    model = Pagina
    success_url = reverse_lazy('pagina_lista')
    fields=['titulo', 'subtitulo', 'cuerpo', 'imagen']
    template_name="pagina_update.html"

"""class PaginaUpdate(LoginRequiredMixin,UpdateView):
    model = Pagina
    success_url = reverse_lazy('pagina_lista')
    fields=['titulo', 'subtitulo', 'cuerpo', 'imagen']
    template_name="pagina_update.html"""

class PaginaDelete(LoginRequiredMixin,DeleteView):
    model = Pagina
    success_url = reverse_lazy('pagina_lista')
    template_name="pagina_confirm_delete.html"

class PaginaList(ListView):
    model=Pagina
    template_name="listapaginas.html"
    ordering= ["-fecha_posteo"]

class PaginaDetalle(DetailView):
    model=Pagina
    template_name="pagina_detalle.html"

def obtenerimagen(request):
    lista=Imagen.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/post/defaultpost.png"
    return imagen

def agregarimagen(request):
    if request.method=="POST":
        form=Imagenform(request.POST, request.FILES)
        if form.is_valid():
            imagen=Imagen(user=request.user, imagen=request.FILES["imagen"])
            imagenvieja=Imagen.objects.filter(user=request.user)
            if len(imagenvieja)>0:
                imagenvieja[0].delete()
            imagen.save()
            return render(request, "inicio.html", {"mensaje":f"Avatar agregado correctamente"})
        else:
            return render(request, "pagina_form.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar avatar"})

    else:
        form=Imagenform()
        return render(request, "pagina_form.html", {"form":form, "usuario": request.user})










"""def crearpagina(request):
    if request.method=="POST":
        formulario= paginaform(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            titulo=info["titulo"]
            subtitulo=info["subtitulo"]
            autor=info["autor"]
            cuerpo=info["cuerpo"]
            fecha_posteo=info["fecha_posteo"]
            imagen=info(user=request.user, imagen=request.FILES["imagen"])
            pagina= Pagina(titulo=titulo, subtitulo=subtitulo, autor=autor, cuerpo=cuerpo, fecha_posteo=fecha_posteo, imagen=imagen)
            pagina.save()
            return render(request, "inicio.html", {"mensaje": "Posteo guardado correctamente"})
    else:
        return render(request, "crearpagina.html", {"form": formulario})"""
