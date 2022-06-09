from contacto.views import contactoFormulario
from django.urls import path


urlpatterns = [
    path('contacto/',contactoFormulario, name = 'Contacto'),
   

]