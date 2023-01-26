from django.urls import path
from .views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [


path('registro', registro, name="registro"),
path("login/", login_request, name="login"),
path("logout/", LogoutView.as_view(), name="logout"),

path('sobremi/', sobremi, name="sobremi"),

path("editarcuenta/", editarcuenta, name="editarcuenta"),
path("editarprofile/", editarprofile, name="editarprofile"),
path("agregaravatar/", agregaravatar, name="agregaravatar"),


path("enviarmensaje/", enviarmensaje, name="enviarmensaje"), 
path("buscarmensaje/", buscarmensaje, name="buscarmensaje"),


]
