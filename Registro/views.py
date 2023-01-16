from django.shortcuts import render
from .models import *
from Blog.models import *
from Registro.forms import *
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.defaults import page_not_found



def inicio(request):
        return render (request, "inicio.html")



#CREAR USUARIO TMB LLEVA A REGISTRO Y NO AL INICIO
def registro(request):
    if request.method=="POST":
        form=registrousuarioform(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "registro.html", {"form":form, "mensaje": "Error al crear el usuario"})
    else:
        form= registrousuarioform()
        return render(request, "registro.html", {"form":form})



def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usu=informacion["username"]
            clave=informacion["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None: #(SI ME DEVOLVIO ALGO, si el usuario esta en la base)si no existe devuelve none
                login(request, usuario)  #LOGUEa mi usuario
                return render(request, "inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
                
                    
            else:
                return render(request, "inicio.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "ingresar.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "ingresar.html", {"form":form})




#de aca voy a sacar las pass para hacer un modulo nuevo
@login_required
def editarperfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.first_name=informacion["first_name"]
            usuario.last_name=informacion["last_name"]
            usuario.email=informacion["email"]
            usuario.password1=informacion["password1"]
            usuario.password2=informacion["password2"]
            usuario.web_site=informacion["web_site"]
            usuario.descripcion=informacion["descripcion"]
            
            usuario.save()
            
            return render(request, "inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar": obteneravatar(request)}) 
        else:
            return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})
    
    else:
        form=UserEditform(instance=usuario)
        return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})




def obteneravatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/defaultavatar.jpg"
    return avatar

@login_required
def agregaravatar(request):
    if request.method=="POST":
        form=Avatarform(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarviejo=Avatar.objects.filter(user=request.user)
            if len(avatarviejo)>0:
                #avatarviejo[0].imagen.delete()
                avatarviejo[0].delete()
            avatar.save()
            return render(request, "inicio.html", {"mensaje":f"Avatar agregado correctamente"})
        else:
            return render(request, "agregaravatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar avatar"})

    else:
        form=Avatarform()
        return render(request, "agregaravatar.html", {"form":form, "usuario": request.user})




"""def paginaperfil(request, pk):
	perfil = Pagina.usuario.get(id=pk)
	context = {'perfil':perfil}
	return render(request, 'profile_page.html', context)"""


class PerfilDetalle(DetailView): 
    model=Profile
    template_name="profile_page.html"
