from django import forms

class UsuarioFormulario(forms.Form):
    nombre_de_usuario= forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)

class LoginFormulario(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=20)
    contraseña = forms.CharField(max_length=50)