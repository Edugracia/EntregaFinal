from django.urls import path
from .views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [


path('registro', registro, name="registro"), #sI borro este registro?
path("login/", login_request, name="login"),
path("logout/", LogoutView.as_view(), name="logout"),
path("editarperfil/", editarperfil, name="editarperfil"),
#path('profile/<pk>', views.PerfilDetalle.as_view(), name="profile"),

path('profile/<pk>', views.profile, name="profile"), #probando esta
path("agregaravatar/", agregaravatar, name="agregaravatar"),

path("leerusuarios/", views.UserListView.as_view(), name="leerusuarios"),
#path('leerusuarios/', views.leerusuarios, name="leerusuarios"),
path("enviarmensaje/", enviarmensaje, name="enviarmensaje"),
path("buscarmensaje/", buscarmensaje, name="buscarmensaje"),
#path("buscarmensaje/", buscarmensaje, name="buscarmensaje"),

]

#REVISAR PORQUE DESPUES DE LOGEARME ME LLEVA A REGISTRO/LOGUIN Y NI AL INICIO


"""path('pagina/<pk>', PaginaDetalle.as_view(), name="pagina_detalle"),"""


"""path('paginaperfil/<pk>', views.paginaperfil, name="paginaperfil"),"""