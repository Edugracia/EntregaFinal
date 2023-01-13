from django.urls import path, include
from .views import *
from Registro.views import *



urlpatterns = [ 
    #SAQUE EL INICIO DE ACA
    path('nuevopost/', nuevopost, name="nuevopost"),
    path('editarpagina/<id>', editarpagina, name="editarpagina"),  #(CON EL ID ANDA queda ver la form para editar)le clave el pk si se lo pongo entra a la lista, pero si se lo saco se rompe el boton editar
    path("agregarimagen/", agregarimagen, name="agregarimagen"),
    path('pagina/borrar/<pk>', PaginaDelete.as_view(), name="pagina_borrar"),
    path('pagina/list/', PaginaList.as_view(), name="pagina_lista"),
    path('pagina/<pk>', PaginaDetalle.as_view(), name="pagina_detalle"),   

]

"""path('', inicio, name="inicio"),"""
"""path('pagina/nueva/', PaginaCreacion.as_view(), name="pagina_crear"),"""
"""path('pagina/editar/<pk>', PaginaUpdate.as_view(), name="pagina_editar"),"""