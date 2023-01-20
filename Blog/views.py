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



#PAGINAS

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
            pagina= Pagina(user=usuario, titulo=titulo, subtitulo=subtitulo, imagen=imagen, cuerpo=cuerpo)
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



class PaginaDelete(LoginRequiredMixin,DeleteView):
    model = Pagina
    success_url = reverse_lazy('leerpaginas')
    template_name="pagina_confirm_delete.html"

class PaginaList(ListView):
    model=Pagina
    template_name="listapaginas.html"
    ordering= ["-fecha_posteo"]



def leerpaginas(request):
    paginas=Pagina.objects.all()
    return render(request, "listapaginas_copia.html", {"paginas":paginas})  #probando cambio, la comentada de abajo era la anteior



def paginadetalle(request, pk):
	pagina = Pagina.objects.get(id=pk)
	context = {'pagina':pagina}
	return render(request, 'pagina_detalle.html', context)

