# Generated by Django 4.1.3 on 2023-01-18 00:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registro', '0032_alter_mensajesalida_emisor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mensajesalida',
            new_name='Mensaje',
        ),
        migrations.DeleteModel(
            name='Mensajeentrada',
        ),
    ]
