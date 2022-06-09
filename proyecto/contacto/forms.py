from django import forms

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    texto = forms.CharField(max_length=500)
