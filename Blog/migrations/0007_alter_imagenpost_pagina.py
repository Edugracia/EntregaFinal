# Generated by Django 4.1.3 on 2023-01-11 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_rename_autor_imagenpost_pagina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenpost',
            name='Pagina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.pagina'),
        ),
    ]
