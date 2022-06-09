from django.shortcuts import render
from contacto.models import Contacto
from contacto.forms import ContactoFormulario

def contactoFormulario(request):
    if request.method == 'POST':
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            contacto = Contacto(nombre = info['nombre'], apellido = info['apellido'], nombre_de_usuario = info['nombre_de_usuario'], email = info['email'], texto = info['texto'])
            contacto.save()
            return render(request,'inicio.html')
    else:
        formulario = ContactoFormulario()
    return render(request,'contacto.html',{'formulario': formulario})

