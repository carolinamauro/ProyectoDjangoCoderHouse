from django.shortcuts import render
from django.shortcuts import render
from login.forms import  UsuarioFormulario,LoginFormulario
from login.models import Usuario
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth


def registrarUsuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = Usuario(nombre = info['nombre'], apellido = info['apellido'],nombre_de_usuario = info['nombre_de_usuario'], email = info['email'], contraseña = info['contraseña'])
            usuario.save()
            return render(request,'inicio.html') #ver
    else:
        formulario = UsuarioFormulario()
    return render(request,'registro.html',{'formulario': formulario})

def login(request):
    if request.method == 'POST':
        form = LoginFormulario(request.POST)
        if form is not None:
            user = auth.authenticate(username=form['nombre_de_usuario'], password=form['contraseña'])
            if user is not None:
               auth.login(request, user)
               return render(request,'inicio.html') 
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login.html')
    else:
        form = LoginFormulario()
    return render(request, 'login.html',{'form':form})


