from django.urls import path, include
from .views import *
from . import views
from Registro.views import * 



urlpatterns = [ 
    #SAQUE EL INICIO DE ACA
    path('nuevopost/', nuevopost, name="nuevopost"), 
    path('editarpagina/<id>', editarpagina, name="editarpagina"),
    path('pagina/borrar/<pk>', PaginaDelete.as_view(), name="pagina_borrar"),
    path('paginadetalle/<pk>', views.paginadetalle, name="paginadetalle"),
    path('leerpaginas/', views.leerpaginas, name="leerpaginas"),
    

]

