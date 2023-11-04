from aplicaciones.pedido.models import Pedido
from aplicaciones.usuario.models import Customer
from aplicaciones.categoria.models import Categoria
from notifications.models import Notification
from django.contrib.auth.decorators import login_required

def carrito_info(request):
    carrito_info = {'cantidad_del_carrito': 0}
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        #Desde aca
        except Customer.DoesNotExist:
            # Si el Customer no existe, crea uno y vincúlalo al usuario actual
            #TODO Revisar en donde hacer esto, en una vista de login o registro, para que se una al campo ONE to ONE entre Customer y Usuario
            customer = Customer.objects.create(user=request.user)
        #hasta aca
        pedido, created = Pedido.objects.get_or_create(customer=customer)
    # Aquí, obtén la información del carrito y devuelve un diccionario con los datos relevantes.
        if pedido:
            carrito_info = {
            'cantidad_del_carrito': pedido.get_cart_items,
        # Otras datos del carrito
    }
    return {'carrito_info': carrito_info}


def categorias_context(request):
    categorias = Categoria.objects.all()
    return {
        'categorias': categorias,
    }

def notificaciones_lista_context(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    else:
        notifications = [] 
    return {'notifications': notifications}
