from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from Portafolio.forms import ContactoFormulario, UsuarioFormulario,LoginFormulario
from Portafolio.models import Contacto, Usuario
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def inicio(self):
    plantilla = loader.get_template('Portafolio/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento) 

def contactoFormulario(request):
    if request.method == 'POST':
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            contacto = Contacto(nombre = info['nombre'], apellido = info['apellido'], nombre_de_usuario = info['nombre_de_usuario'], email = info['email'], texto = info['texto'])
            contacto.save()
            return render(request,'Portafolio/inicio.html')
    else:
        formulario = ContactoFormulario()
    return render(request,'Portafolio/contacto.html',{'formulario': formulario})

def testimonios(request):
    return render(request,'Portafolio/testimonios.html')

def registrarUsuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = Usuario(nombre = info['nombre'], apellido = info['apellido'],nombre_de_usuario = info['nombre_de_usuario'], email = info['email'], contraseña = info['contraseña'])
            usuario.save()
            return render(request,'Portafolio/inicio.html') #ver
    else:
        formulario = UsuarioFormulario()
    return render(request,'Portafolio/registro.html',{'formulario': formulario})

#def login(request):
#    if request.method == 'POST':
#        form = LoginFormulario(request.POST)
#        if form is not None:
#            user = auth.authenticate(username=form['nombre_de_usuario'], password=form['contraseña'])
#            if user is not None:
#               auth.login(request, user)
#               return render(request,'Portafolio/inicio.html') 
#        else:
#            messages.info(request, 'Invalid Username or Password')
#            return redirect('Portafolio/login.html')
#    else:
#        form = LoginFormulario()
#    return render(request, 'Portafolio/inicio.html',{'form':form})
#
#
#def logout_user(request):
#    auth.logout(request)
#    return redirect('inicio')