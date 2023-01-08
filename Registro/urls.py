from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
path('', inicio, name="inicio"),

path("registro/", registro, name="registro"),
path("login/", login_request, name="login"),
path("logout/", LogoutView.as_view(), name="logout"),
]






"""path("editarperfil/", editarperfil, name="editarperfil"),
path("agregaravatar/", agregaravatar, name="agregaravatar"),"""