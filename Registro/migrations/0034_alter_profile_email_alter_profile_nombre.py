# Generated by Django 4.1.3 on 2023-01-21 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0033_rename_mensajesalida_mensaje_delete_mensajeentrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]