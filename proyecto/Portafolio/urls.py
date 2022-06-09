from Portafolio.views import inicio,contactoFormulario,testimonios, registrarUsuario,logout_user,login
from django.urls import path,include


urlpatterns = [
    path('',inicio ),
    path('contacto/',contactoFormulario, name = 'Contacto'),
    path('testimonios/',testimonios,name="Testimonios"),
    #path('registro/',registrarUsuario,name="Registro"),
    #path("register/", register, name="register"),
    #path("login/", login, name="IniciarSesion"),
    path("logout_user", logout_user, name="logout_user"),
    
    #path('iniciarSesion/',login, {'template_name':'iniciar_sesion.html'},name="IniciarSesion"),
    
    
]

