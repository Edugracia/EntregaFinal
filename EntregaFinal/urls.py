
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Blog.views import *
from Registro.views import *

#Importe al ultimo las vistas de las dos apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"), #LO PUOSE ACA
    path('blog/', include ("Blog.urls")), #LE PUSE EL BLOG/ ACA
    path('registro/', include ("Registro.urls")),  #SI BORRO REGISTRO SE ROMPE EL SALIR y el boton salir no hace nada
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

"""path('', include ("Registro.urls")),"""