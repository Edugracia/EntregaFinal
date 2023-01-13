from django.shortcuts import render
from .models import *
from Registro.models import *
from Blog.forms import *
from Registro.forms import *
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
    autor= request.user
    if request.method=="POST":
        formulario=nuevopostform(request.POST)
        if formulario.is_valid():            
            informacion= formulario.cleaned_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]            
            cuerpo= informacion["cuerpo"]
            pagina= Pagina(autor=autor, titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo)
            pagina.save()
            posteos=Pagina.objects.all()
            return render(request, "pagina_detalle.html", {"posteos": posteos, "mensaje": "Blog guardado"})
        else:
            return render(request, "pagina_form_copia.html", {"mensaje": "Informacion no Valida"})
    else:
        formulario=nuevopostform()
        return render(request, "pagina_form_copia.html", {"formulario": formulario})


def obtenerimagen(request):
    lista=Imagenpagina.objects.filter(user=request.user)
    if len(lista)!=0:
        imagenpagina=lista[0].imagen.url
    else:
        imagenpagina="/media/post/defaultpost.png"
    return imagenpagina

def agregarimagen(request):
    if request.method=="POST":
        form=Imagenpaginaform(request.POST, request.FILES)
        if form.is_valid():
            imagenpagina=Imagenpagina(user=request.user, imagen=request.FILES["imagen"])
            imagenpaginavieja=Imagenpagina.objects.filter(user=request.user)
            if len(imagenpaginavieja)>0:
                imagenpaginavieja[0].delete()
            imagenpagina.save()
            return render(request, "pagina_detalle.html")
        else:
            return render(request, "agregar_Imagen.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar imagen"})

    else:
        form=Imagenpaginaform()
        return render(request, "agregar_Imagen.html", {"form":form, "usuario": request.user})


def editarpagina(request, id):
    pagina=Pagina.objects.get(id=id) #ver si esto va por get o post
    if request.method=="POST":
        form=EditarPagform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            pagina.titulo=informacion["titulo"]
            pagina.subtitulo=informacion["subtitulo"]
            pagina.cuerpo=informacion["cuerpo"]
            pagina.save()
            return render(request, "pagina_detalle.html", {"mensaje":f"Pagina editada correctamente", "form":form, "pagina":pagina, "imagenpagina": obtenerimagen(request)})
        else:
            return render(request, "pagina_update.html", {"form":form, "pagina":pagina, "imagenpagina": obtenerimagen(request)})
    
    else:
        form=EditarPagform(initial={"titulo":pagina.titulo, "subtitulo":pagina.subtitulo, "cuerpo":pagina.cuerpo})
        return render(request, "pagina_update.html", {"form":form, "pagina":pagina, "imagenpagina": obtenerimagen(request)})

#Vistas de paginas

"""class PaginaCreacion(LoginRequiredMixin,CreateView):
    model = Pagina
    template_name="pagina_form.html"
    success_url = reverse_lazy('pagina_lista')
    fields=['titulo', 'subtitulo', 'autor', 'cuerpo', 'imagen']"""

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
