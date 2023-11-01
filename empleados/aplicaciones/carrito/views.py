from django.shortcuts import render
from django.http import JsonResponse
import json
from aplicaciones.pedido.models import Pedido
from aplicaciones.producto.models import Producto
from .models import Carrito

def carrito(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        pedido, created = Pedido.objects.get_or_create(customer=customer)
        items = pedido.carrito_set.all()
        # pedido es la foreign key de carrito
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'carrito/carrito.html', context)

def pago(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        pedido, created = Pedido.objects.get_or_create(customer=customer)
        items = pedido.carrito_set.all()
        # pedido es la foreign key de carritoproducto
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'carrito/pago.html', context)




def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('Producto ID:', productId)
    
    customer = request.user.customer
    producto = Producto.objects.get(id=productId)
    pedido, created = Pedido.objects.get_or_create(customer=customer)
    carrito, created = Carrito.objects.get_or_create(pedido=pedido, producto=producto)
    
    if action == 'add':
        carrito.cantidad = (carrito.cantidad + 1)
    elif action == 'remove':
        carrito.cantidad = (carrito.cantidad - 1)
        
    carrito.save()
    
    if carrito.cantidad <= 0:
        carrito.delete()
    
    return JsonResponse('Item was added', safe=False)
