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
    usuario= request.user
    if request.method=="POST":
        formulario=nuevopostform(request.POST, request.FILES)
        if formulario.is_valid():            
            informacion= formulario.cleaned_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            imagen= informacion["imagen"]
            cuerpo= informacion["cuerpo"]
            pagina= Pagina(usuario=usuario, titulo=titulo, subtitulo=subtitulo, imagen=imagen, cuerpo=cuerpo)
            pagina.save()
            
            return render(request, "pagina_detalle.html", {"pagina": pagina, "mensaje": "Blog guardado"})
        else:
            return render(request, "pagina_form_copia.html", {"mensaje": "Informacion no Valida"})
    else:
        formulario=nuevopostform()
        return render(request, "pagina_form_copia.html", {"formulario": formulario})



@login_required
def editarpagina(request, id):
    pagina=Pagina.objects.get(id=id) #ver si esto va por get o post
    if request.method=="POST":
        formulario=EditarPagform(request.POST, request.FILES)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            pagina.titulo=informacion["titulo"]
            pagina.subtitulo=informacion["subtitulo"]
            pagina.imagen=informacion["imagen"]
            pagina.cuerpo=informacion["cuerpo"]
            
            pagina.save()
            pass
            return render(request, "pagina_detalle.html", {"pagina":pagina})
        
    else:
        formulario=EditarPagform(initial={"titulo":pagina.titulo, "subtitulo":pagina.subtitulo, "cuerpo":pagina.cuerpo})
        return render(request, "pagina_update.html", {"formulario":formulario, "pagina":pagina})


"""def obtenerimagen(request):
    lista=Imagenpagina.objects.filter(pagina=request.pagina.id)
    if len(lista)!=0:
        imgpost=lista[0].imgpost.url
    else:
        imgpost=""
    return imgpost"""

"""def obtenerimagen(request):
    lista=Imagenpagina.objects.filter(pagina_id = request.user.pagina)
    if len(lista)!=0:
        imgpost=lista[0].imgpost.url
    else:
        imgpost=""
    return imgpost"""




"""@login_required
def agregarimagen(request):
    if request.method=="POST":
        form=Imagenpaginaform(request.POST, request.FILES)
        if form.is_valid():
            imgpost=Imagenpagina(user=request.user, imgpost=request.FILES["imgpost"])
            imgpostvieja=Imagenpagina.objects.filter(user=request.user)
            if len(imgpostvieja)>0:
                imgpostvieja[0].delete()
            imgpost.save()
            return render(request, "pagina_detalle.html", {"imgpost": obtenerimagen(request)})
        

    else:
        form=Imagenpaginaform()  #####saque esto instance=imgpost
        return render(request, "agregar_Imagen.html", {"form":form, "imgpost": request.pagina})"""




"""@login_required
def agregarimagen(request):
    if request.method=="POST":
        form=Imagenpaginaform(request.POST, request.FILES)
        if form.is_valid():
            i=Pagina.objects.get(pagina_id=request.imgpost)
            imagenposteo=Imagenpagina (pagina=i, imgpost=form.cleaned_data["imgpost"])

            
            imagenposteo.save()
            return render(request, "inicio.html")


    else:
        form=Imagenpaginaform()  #####saque esto instance=imgpost
        return render(request, "agregar_Imagen.html", {"form":form})

#Esta es la que tenia antes de todo
@login_required
def agregarimagen(request):
    if request.method=="POST":
        form=Imagenpaginaform(request.POST, request.FILES)
        if form.is_valid():
            imgpost=Imagenpagina(user=request.user, imgpost=request.FILES["imgpost"])
            imgpostvieja=Imagenpagina.objects.filter(user=request.user)
            if len(imgpostvieja)>0:
                imgpostvieja[0].delete()
            imgpost.save()
            return render(request, "pagina_detalle.html", {"imgpost": obtenerimagen(request)})
        

    else:
        form=Imagenpaginaform()  #####saque esto instance=imgpost
        return render(request, "agregar_Imagen.html", {"form":form, "imgpost": request.pagina})"""




"""@login_required
def editarpagina(request, id):
    pagina=Pagina.objects.get(id=id) #ver si esto va por get o post
    if request.method=="POST":
        formulario=EditarPagform(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            pagina.titulo=informacion["titulo"]
            pagina.subtitulo=informacion["subtitulo"]
            pagina.cuerpo=informacion["cuerpo"]
            pagina.save()
            return render(request, "pagina_detalle.html", {"pagina":pagina})
        pass
    else:
        formulario=EditarPagform(initial={"titulo":pagina.titulo, "subtitulo":pagina.subtitulo, "cuerpo":pagina.cuerpo})
        return render(request, "pagina_update.html", {"formulario":formulario, "pagina":pagina})"""




"""def editarpagina(request, id):
    pagina=Pagina.objects.get(id=id) #ver si esto va por get o post
    if request.method=="POST":
        form=EditarPagform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            pagina.titulo=informacion["titulo"]
            pagina.subtitulo=informacion["subtitulo"]
            pagina.cuerpo=informacion["cuerpo"]
            pagina.save()
            return render(request, "pagina_detalle.html", {"form":form, "pagina":pagina.pagina, "imgpost": obtenerimagen(request)})
        else:
            return render(request, "pagina_update.html", {"form":form, "pagina":pagina.pagina, "imgpost": obtenerimagen(request)})
    
    else:
        form=EditarPagform(initial={"titulo":pagina.titulo, "subtitulo":pagina.subtitulo, "cuerpo":pagina.cuerpo})
        return render(request, "pagina_update.html", {"form":form, "pagina":pagina.pagina, "imgpost": obtenerimagen(request)})"""








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
    success_url = reverse_lazy('leerpaginas')
    template_name="pagina_confirm_delete.html"

class PaginaList(ListView):
    model=Pagina
    template_name="listapaginas.html"
    ordering= ["-fecha_posteo"]

"""class PaginaDetalle(DetailView):
    model=Pagina
    template_name="pagina_detalle.html" 
    
    
    imgpost= obtenerimagen(request)""" #VER COMO PASARLE DE CONTEXTO LA IMAGEN"""

def leerpaginas(request):
    paginas=Pagina.objects.all()
    return render(request, "listapaginas_copia.html", {"paginas":paginas})  #probando cambio, la comentada de abajo era la anteior


"""def paginadetalle(request, id=id):
    pagina=Pagina.objects.get(id=id)
    contexto={"pagina":pagina}
    return render(request, "pagina_detalle.html", contexto) #ESTO ESTARIA ("imgpost":obtenerimagen(request))QUEDA VER EL DRAMA DEL OBTENER IMAGEN DE ARRIBA"""


def paginadetalle(request, pk):
	pagina = Pagina.objects.get(id=pk)
	context = {'pagina':pagina}
	return render(request, 'pagina_detalle.html', context)



"""def leerpaginas(request):
    paginas=Pagina.objects.all()
    contexto={"paginas":paginas}
    return render(request, "listapaginas_copia.html", contexto)"""





#asi anda
"""def paginadetalle(request, id=id):
    pagina=Pagina.objects.get(id=id)
    context={"pagina":pagina}
    return render(request, "pagina_detalle.html", context)"""

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
