from django.shortcuts import render
from .models import Pagina
from Blog.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def inicio(request):
    return render (request, "inicio.html")

def blogs(request):
    return render (request, "blogs.html")

@login_required
def nuevopost(request):
    if request.method=="POST":
        formulario=nuevopostform(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            #imagen= informacion["imagen"]
            cuerpo= informacion["cuerpo"]
            pag= Pagina(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo)
            pag.save()
            posteos=Pagina.objects.all()
            return render(request, "pagina_detalle.html", {"posteos": posteos, "mensaje": "Blog guardado"})
        else:
            return render(request, "pagina_form_copia.html", {"mensaje": "Informacion no Valida"})
    else:
        formulario=nuevopostform()
        return render(request, "pagina_form_copia.html", {"formulario": formulario})




#Vistas de paginas

class PaginaCreacion(LoginRequiredMixin,CreateView):
    model = Pagina
    template_name="pagina_form.html"
    success_url = reverse_lazy('pagina_lista')
    fields=['titulo', 'subtitulo', 'autor', 'cuerpo', 'imagen']

class PaginaUpdate(LoginRequiredMixin,UpdateView):
    model = Pagina
    success_url = reverse_lazy('pagina_lista')
    fields=['titulo', 'subtitulo', 'cuerpo', 'imagen']
    template_name="pagina_update.html"

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
