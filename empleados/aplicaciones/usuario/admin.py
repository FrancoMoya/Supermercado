from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        user, created = User.objects.get_or_create(username=obj.nombre)  # Puedes personalizar esto según tus necesidades
        obj.user = user
        super().save_model(request, obj, form, change)

admin.site.register(Customer, CustomerAdmin)