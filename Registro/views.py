from django.shortcuts import render
from .models import *
from Blog.models import *
from Registro.forms import *
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
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



#de momento esta nueva simplificada re va
#de aca voy a sacar las pass para hacer un modulo nuevo
"""@login_required
def editarperfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditform(request.POST, instance=usuario)
        if form.is_valid():
                        
            usuario.save()
            
            return render(request, "inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar": obteneravatar(request)}) 
        else:
            return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})
    
    else:
        form=UserEditform(instance=usuario)
        return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})"""


@login_required
def editarperfil(request):  #VER TEMA DE LA EDICION DE PERFIL CON LA DE USUARIO
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
            usuario.set_password(str(usuario.password1))
            usuario.save()
            
            return render(request, "profile_page.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar": obteneravatar(request)}) 
        else:
            return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})
    
    else:
        form=UserEditform(instance=usuario)
        return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})



#ESTA ANDA VOY A PROBAR OTRA ARRIBA A VER SI CONSIGO QUE MEUSTRE LOS DATOS A EDITAR

"""@login_required
def editarperfil(request):  #VER TEMA DE LA EDICION DE PERFIL CON LA DE USUARIO
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
            usuario.set_password(str(usuario.password1))
            usuario.save()
            
            return render(request, "profile_page.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar": obteneravatar(request)}) 
        else:
            return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})
    
    else:
        form=UserEditform(instance=usuario)
        return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})
"""

@login_required
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







class PerfilDetalle(DetailView): 
    model=Profile   #Y SI USO EL MODELO USER?
    template_name="profile_page.html"



def paginadetalle(request, pk):
	pagina = Pagina.objects.get(id=pk)
	context = {'pagina':pagina}
	return render(request, 'pagina_detalle.html', context)


def profile(request, pk):   
    user=User.objects.get(id=pk)
    profile=Profile.objects.filter(user=user.id).get() #estoy pidiendo todos los objetos de profile de este user
    lista=Avatar.objects.filter(user=user.id)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/defaultavatar.jpg"        
    
    return render(request, "profile_page.html", {"profile":profile, "avatar":avatar})



"""def profile(request, pk):   #ESTA ES LA QUE VA
    user=User.objects.get(id=pk)
    profile=Profile.objects.filter(user=user.id).get()
    
    return render(request, "profile_page.html", {"profile":profile})"""



#probando lista de usuarios para el envio de mensajes

"""class UserListView(LoginRequiredMixin, generic.ListView):  #esto anda toca ver como linkear a la vista enviar mensaje
    model=User
    template_name="lista_usuarios.html"""



"""@login_required
def buscarmensaje(request):  #creo ya anda piola
    receptor= request.user
    if receptor != "":
        mensajes=Mensaje.objects.filter(receptor=receptor) #aca hay que filtrar por receptor
        return render(request, "mensajes_recibidos.html", {"mensajes":mensajes}) #poner un else diciendo que no tiene mensajes"""



@login_required
def buscarmensaje(request):
    receptor= request.user
    if receptor != "":
        mensajes=Mensaje.objects.filter(receptor=receptor) 
        return render(request, "mensajes_recibidos.html", {"mensajes":mensajes}) #poner un else diciendo que no tiene mensajes"





@login_required
def enviarmensaje(request):
    if request.method=="POST":
        form= MensajeForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            emisor= informacion["emisor"]
            receptor= informacion["receptor"]
            cuerpo= informacion["cuerpo"]
            mensaje= Mensaje(emisor=emisor, receptor=receptor, cuerpo=cuerpo)
            mensaje.save()
            return render(request, "mensaje_salida.html", {"mensaje": "Mensaje enviado"})
        else:
            return render(request, "mensaje_salida.html", {"mensaje": "Informacion no Valida"})
    else:
        formulario= MensajeForm()
        return render(request, "mensaje_salida.html", {"form": formulario})


"""def enviarmensaje(request, id): #si me llamas a enviarmensaje con un 3 traeme de la base todo receptor que su id sea 3
    if request.method=="POST":
        emisor=request.user
        receptor=User.objects.get(id=id) #aca cambie por id y me lo mando ami mismo #revisar a ver si no hay que filtrar como con buscarmensaje
        #para que haya un receptor, primero tiene que haber un mensaje
        formulario= Mensajeform(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            cuerpo=informacion["cuerpo"]
            mensaje=Mensaje(emisor=emisor, receptor=receptor, cuerpo=cuerpo)
            mensaje.save()
            return render(request, "mensaje_salida.html", {"mensaje": f"Mensaje enviado a {receptor} correctamente"})
        else:
            return render(request, "mensaje_salida.html", {"mensaje": "Informacion no Valida"})
    else:
        formulario=Mensajeform()
        return render(request, "mensaje_salida.html", {"formulario": formulario})"""