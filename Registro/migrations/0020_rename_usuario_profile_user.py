# Generated by Django 4.1.3 on 2023-01-16 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0019_rename_usuario_avatar_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='usuario',
            new_name='user',
        ),
    ]
