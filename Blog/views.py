from django.shortcuts import render
from .models import *
from Registro.models import *
from Blog.forms import *
from Registro.forms import *
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




def inicio(request):
    return render (request, "inicio.html")

def blogs(request):
    return render (request, "blogs.html")



#PAGINAS (posteos)

@login_required
def nuevopost(request):
    usuario= request.user
    if request.method=="POST":
        formulario= nuevopostform(request.POST, request.FILES)
        if formulario.is_valid():            
            informacion= formulario.cleaned_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            imagen= informacion["imagen"]
            cuerpo= informacion["cuerpo"]
            pagina= Pagina(user=usuario, titulo=titulo, subtitulo=subtitulo, imagen=imagen, cuerpo=cuerpo)
            pagina.save()
            
            return render(request, "pagina_detalle.html", {"pagina": pagina, "mensaje": "Blog guardado"})
        else:
            return render(request, "pagina_form_copia.html", {"mensaje": "Informacion no Valida"})
    else:
        formulario= nuevopostform()
        return render(request, "pagina_form_copia.html", {"formulario": formulario})



@login_required
def editarpagina(request, id):
    pagina= Pagina.objects.get(id=id) 
    if request.method=="POST":
        formulario= EditarPagform(request.POST, request.FILES)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            pagina.titulo=informacion["titulo"]
            pagina.subtitulo=informacion["subtitulo"]
            pagina.imagen=informacion["imagen"]
            pagina.cuerpo=informacion["cuerpo"]
            
            pagina.save()
            pass
            return render(request, "pagina_detalle.html", {"pagina":pagina})
        
    else:
        formulario= EditarPagform(initial={"titulo":pagina.titulo, "subtitulo":pagina.subtitulo, "cuerpo":pagina.cuerpo})
        return render(request, "pagina_update.html", {"formulario":formulario, "pagina":pagina})



class PaginaDelete(LoginRequiredMixin,DeleteView):
    model= Pagina
    success_url= reverse_lazy('leerpaginas')
    template_name="pagina_confirm_delete.html"



def leerpaginas(request):
    paginas= Pagina.objects.all()
    return render(request, "listapaginas.html", {"paginas":paginas}) 



def paginadetalle(request, pk):
	pagina= Pagina.objects.get(id=pk)
	context= {'pagina':pagina}
	return render(request, 'pagina_detalle.html', context)


def obtenerperfil(request, pk):
    user= User.objects.get(id=pk)
    profile= Profile.objects.filter(user=user.id).get()
    lista= Avatar.objects.filter(user=user.id)
    if len(lista)!= 0:
        avatar= lista[0].imagen.url
    else:
        avatar= "/media/avatars/defaultavatar.jpg"
    return render(request, "profile_page.html", {"profile":profile, "avatar":avatar})


