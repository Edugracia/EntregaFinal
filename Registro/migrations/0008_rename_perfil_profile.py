# Generated by Django 4.1.3 on 2023-01-09 23:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registro', '0007_rename_profile_perfil'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perfil',
            new_name='Profile',
        ),
    ]
