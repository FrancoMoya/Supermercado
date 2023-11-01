"""
URL configuration for empleados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
#Importo la vista
#from aplicaciones.empleado.views import IndexView, PruebaListVIew, ProductosView
from aplicaciones.usuario.views import home, registro, cerrar_sesion, iniciar_sesion
from aplicaciones.carrito.views import updateItem, carrito, pago
from aplicaciones.producto.views import productos, productosItems
from aplicaciones.categoria.views import categorias
from aplicaciones.descuentos.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    #path('home/', IndexView.as_view(), name = 'home'),
    #path('productos/', ProductosView.as_view(), name = 'productos'),
    #path('lista/', PruebaListVIew.as_view()),
    path('', home, name = 'home'),
    path('registro/', registro, name = 'registro'),
    path('productos/', productos, name = 'productos'),
    path('productosItems/', productosItems, name = 'productosItems'),
    path('logout/', cerrar_sesion, name = 'logout'),
    path('login/', iniciar_sesion, name = 'login'),
    path('update_item/', updateItem, name = 'updateItem'),
    path('carrito/', carrito, name = 'carrito'),
    path('pago/', pago, name = 'pago'),
    path('categorias/<str:nombre_categoria>/', categorias, name = 'categorias'),
    path('notificaciones/', notificaciones_lista, name='notificaciones_lista'),
    path('notificaciones/<int:notificacion_id>/', notificacion_detalle, name='notificacion_detalle'),
    path('crear_cupon/', crear_cupon, name='crear_cupon'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
