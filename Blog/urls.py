from django.urls import path, include
from .views import *



urlpatterns = [ 
    path('', inicio, name="inicio"),
    path('pagina/nueva/', PaginaCreacion.as_view(), name="pagina_crear"),
    path('pagina/editar/<pk>', PaginaUpdate.as_view(), name="pagina_editar"),
    path('pagina/borrar/<pk>', PaginaDelete.as_view(), name="pagina_borrar"),
    path('pagina/list/', PaginaList.as_view(), name="pagina_lista"),
    path('pagina/<pk>', PaginaDetalle.as_view(), name="pagina_detalle"),   

]

"""path('', inicio, name="inicio"),"""