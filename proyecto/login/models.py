from django.db import models

class Login(models.Model):
    nombre_de_usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=50)

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nombre_de_usuario = models.CharField(max_length=20)
    email = models.EmailField()
    contraseña = models.CharField(max_length=50)