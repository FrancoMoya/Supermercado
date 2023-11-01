from django.shortcuts import render, get_object_or_404, redirect
from notifications.models import Notification
from aplicaciones.usuario.models import Customer
from .models import Cupon
import secrets, string
from django.contrib.auth.decorators import login_required

def generar_codigo_aleatorio(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for i in range(length))

def notificar_a_todos_los_usuarios_sobre_cupon(cupon):
    usuarios = Customer.objects.all()
    mensaje = f"Nuevo cupón disponible: {cupon.codigo} (compartido)"
    for customer in usuarios:
        user = customer.user
        Notification.objects.create(
            actor=Cupon,
            recipient=user,
            verb='nuevo_cupon',
            description=mensaje,
            target=cupon,
        )

@login_required
def crear_cupon(request):
    if request.method == 'POST':
        compartido = request.POST.get('compartido', False)
        codigo = request.POST.get('codigo', None)
        if not codigo:
            codigo = generar_codigo_aleatorio()
        compartido = compartido == "on"
        usuarios_asociados = request.POST.getlist('usuarios_asociados')
        # Si el cupón es compartido y no se seleccionaron usuarios, selecciona a todos
        if compartido and not usuarios_asociados:
            usuarios_asociados = Customer.objects.all()
        
        cupon = Cupon(codigo=codigo, compartido=compartido)
        # ... Completa el resto de los campos y guarda el cupón
        
        # Establecer el actor como el usuario administrador actual
        cupon.actor = request.user
        cupon.save()

        if not compartido and usuarios_asociados:
            for usuario_id in usuarios_asociados:
                usuario = Customer.objects.get(id=usuario_id)
                mensaje = f"Nuevo cupón disponible: {cupon.codigo} (exclusivo)"
                Notification.objects.create(
                    actor=Cupon,
                    recipient=usuario.user,
                    verb='nuevo_cupon',
                    description=mensaje,
                    target=cupon,
                )
        elif compartido:
            notificar_a_todos_los_usuarios_sobre_cupon(cupon)

        return redirect('notificaciones_lista')

    # Renderiza la página de creación del cupón
    return render(request, 'descuentos/crear_cupon.html')

def notificaciones_lista(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'usuario/notificaciones_lista.html', {'notifications': notifications})

def notificacion_detalle(request, notificacion_id):
    notification = get_object_or_404(Notification, id=notificacion_id)
    return render(request, 'usuario/notificacion_detalle.html', {'notification': notification})
