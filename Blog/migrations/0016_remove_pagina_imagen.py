# Generated by Django 4.1.3 on 2023-01-15 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0015_pagina_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagina',
            name='Imagen',
        ),
    ]