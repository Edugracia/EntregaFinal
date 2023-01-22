from django.shortcuts import render
from .models import *
from Blog.models import *
from Registro.forms import *
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required




def inicio(request):
        return render (request, "inicio.html")

def sobremi(request):
    
    return render (request, "aboutme.html", {"avatar": obteneravatar(request)})




#registro y login

def registro(request):#esta es la que va
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
                return render(request, "ingresar.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "ingresar.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "ingresar.html", {"form":form})





#PERFILES

#EDICION USUARIO
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

            usuario.set_password(str(usuario.password1))
            usuario.save()
            
            return render(request, "ingresar.html", {"mensaje":f"{usuario.username} editado correctamente", "form":AuthenticationForm(request, data=request.POST)})       
        else:
            return render(request, "editar_perfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obteneravatar(request)})
    
    else:
        form=UserEditform(initial={"first_name":usuario.first_name, "last_name":usuario.last_name, "email":usuario.email})
        return render(request, "editar_perfil.html", {"form":form, "usuario":usuario, "avatar": obteneravatar(request)})





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




def paginadetalle(request, pk):
	pagina = Pagina.objects.get(id=pk)
	context = {'pagina':pagina}
	return render(request, 'pagina_detalle.html', context)




<<<<<<< HEAD
"""def profile(request, pk):     #ESTE ES UN INVENTO
    user=User.objects.get(id=pk)
    if Profile is None:
        if request.method=="POST":
            form=ProfileCreation(request.POST)
            if form.is_valid():
                profile=Profile(user=request.user)
                profile.save()


    profile=Profile.objects.filter(user=user.id).get()
    lista=Avatar.objects.filter(user=user.id)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/defaultavatar.jpg"        
    
    return render(request, "profile_page.html", {"profile":profile, "avatar":avatar})"""




#CREAR UN BOTON DE CREAR PERFIL Y SI PERFIL IS NOT NONE NO MUESTRE EL BOTON

"""def crearprofile(request):  #ESTO ANDA
    user=request.user
    if request.method=="POST":
        form= Profileform(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre= informacion["nombre"]
            descripcion= informacion["descripcion"]
            email= informacion["email"]
            web_site= informacion["web_site"]
            profile= Profile(user=user, nombre=nombre, descripcion=descripcion, email=email, web_site=web_site)
            profile.save()
            return render(request, "inicio.html", {"mensaje": "Profile creado correctamente"})
        else:
            return render(request, "crear_perfil.html", {"mensaje": "Informacion no Valida", "avatar": obteneravatar(request)})
    else:
        form= Profileform()
        return render(request, "crear_perfil.html", {"form": form, "avatar": obteneravatar(request)})"""


def botonperfil(request):
    user=request.user
    if request.method=="POST":
        form= Profileform(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre= informacion["nombre"]
            descripcion= informacion["descripcion"]
            email= informacion["email"]
            web_site= informacion["web_site"]
            profile= Profile(user=user, nombre=nombre, descripcion=descripcion, email=email, web_site=web_site)
            profile.save()
            pass
            return render(request, "inicio.html", {"mensaje": "Profile creado correctamente"})
    else:
        form=Profileform(initial={"nombre":profile.nombre, "email":profile.email, "web_site":profile.web_site, "descripcion":profile.descripcion})
        return render(request, "editar_perfil.html", {"form":form, "profile":profile})
        





"""    else:
        form=ProfileEditform(initial={"nombre":profile.nombre, "email":profile.email, "web_site":profile.web_site, "descripcion":profile.descripcion})
        return render(request, "editar_perfil.html", {"form":form, "profile":profile})"""

"""def botoncuenta(request):
    user=request.user
    if request.method=="POST":
        cuenta_form=UserEditform(request.POST)
        profile_form=Profileform(request.POST)
        if cuenta_form.is_valid() and profile_form.is_valid():
            user.save()
        return render(request, "ingresar.html", {"mensaje": "editado correctamente"})       
    else:
        
        return render(request, "inicio.html")"""









"""def crearprofile(request):  #ESTA ES LA NUEVA ELIMINA EL PERFIL VIEJO Y CREA UNO NUEVO
    user=request.user
    if request.method=="POST":
        form= Profileform(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre= informacion["nombre"]
            descripcion= informacion["descripcion"]
            email= informacion["email"]
            web_site= informacion["web_site"]
            profile= Profile(user=user, nombre=nombre, descripcion=descripcion, email=email, web_site=web_site)
            profileviejo= Profile.objects.filter(user=request.user)
            if len(profileviejo)>0:
                profileviejo[0].delete()
            profile.save()
            return render(request, "inicio.html", {"mensaje": "Profile creado correctamente"})
        else:
            return render(request, "crear_perfil.html", {"mensaje": "Informacion no Valida", "avatar": obteneravatar(request)})
    else:
        form= Profileform()
        return render(request, "crear_perfil.html", {"form": form, "avatar": obteneravatar(request)})"""





=======
>>>>>>> feature_creoqueanda
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


<<<<<<< HEAD



def profile(request, pk):     #ESTA ES LA QUE VA
    user=User.objects.get(id=pk)
    profile=Profile.objects.filter(user=user.id).get()
    lista=Avatar.objects.filter(user=user.id)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/defaultavatar.jpg"        
    
    return render(request, "profile_page.html", {"profile":profile, "avatar":avatar})



=======
>>>>>>> feature_creoqueanda
#MENSAJERIA

@login_required
def buscarmensaje(request):
    receptor= request.user
    if receptor != "":
        mensajes=Mensaje.objects.filter(receptor=receptor)
        return render(request, "mensajes_recibidos.html", {"mensajes":mensajes})



@login_required
def enviarmensaje(request):
    emisor=request.user
    if request.method=="POST":
        form= MensajeForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            #emisor= informacion["emisor"]
            receptor= informacion["receptor"]
            cuerpo= informacion["cuerpo"]
            mensaje= Mensaje(emisor=emisor, receptor=receptor, cuerpo=cuerpo)
            mensaje.save()
            return render(request, "mensaje_enviado.html", {"mensaje": "Mensaje enviado correctamente"})
        else:
            return render(request, "mensaje_salida.html", {"mensaje": "Informacion no Valida"})
    else:
        formulario= MensajeForm()
        return render(request, "mensaje_salida.html", {"form": formulario})
