from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home (request):
    return render(request, 'usuario/home.html')

def registro (request):
    if request.method == 'GET':
        return render(request, 'usuario/registro.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('productos')
            except IntegrityError:
                return render(request, 'usuario/registro.html',{
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe',
                })
        return render(request, 'usuario/registro.html',{
            'form': UserCreationForm,
            'error': 'Contraseña incorrecta',
            })

def cerrar_sesion (request):
    logout(request)
    return redirect('home')

def iniciar_sesion (request):
    if request.method == 'GET':
        return render(request, 'usuario/login.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'usuario/login.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('productos')
        
