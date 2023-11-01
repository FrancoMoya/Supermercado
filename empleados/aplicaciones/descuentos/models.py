from django.db import models
from aplicaciones.usuario.models import Customer
from django.core.exceptions import ValidationError

def validate_two_digit(value):
    if not (0 <= value <= 99):
        raise ValidationError("El porcentaje debe ser un número de dos dígitos (0-99).")
    
#Para crear cupones que puedan ser utilizados por los usuarios en general(Dejar usuarios_asociados en blanco y compartido en True)
#Para crear cupones que puedan ser utilizados por usuarios o grupos de este en especifico(Seleccionar usuarios_asociados y compartido en False)
class Cupon(models.Model):
    codigo = models.CharField('Código',max_length=20, unique=True, null=True, blank=True)
    fecha = models.DateTimeField('Fecha',auto_now_add=True)
    descuento_porcentaje = models.IntegerField('Porcentaje de descuento', validators=[validate_two_digit], null=True, blank=True)
    descuento_valor = models.IntegerField('Valor de descuento', null=True, blank=True)
    usuarios_asociados = models.ManyToManyField(Customer, blank=True)
    compartido = models.BooleanField('¿Es compartido?',default=True)  # Indica si el cupón es compartido o exclusivo
    # Otros campos relacionados con el cupón (fechas de caducidad, límites de uso, etc.)
    class Meta:
        verbose_name = ('Cupón')
        verbose_name_plural = ('Cupones')
        ordering = ['fecha']
    def __str__(self):
        return f"Código: {self.codigo}"
    