# Generated by Django 4.1.3 on 2023-01-16 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0015_rename_user_profile_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='autor',
            new_name='user',
        ),
    ]
