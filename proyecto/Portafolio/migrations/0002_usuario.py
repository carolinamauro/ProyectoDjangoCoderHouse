# Generated by Django 2.2.12 on 2022-06-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('nombre_de_usuario', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]