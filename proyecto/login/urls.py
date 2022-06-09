from login.views import registrarUsuario,login
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('registro/',registrarUsuario,name="Registro"),
    #path("register/", register, name="register"),logout_user
    path("login/", login, name="Login"),
]