# Generated by Django 4.1.3 on 2023-01-17 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registro', '0024_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajesalida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.CharField(blank=True, max_length=250, null=True)),
                ('enviado', models.DateField(auto_now_add=True)),
                ('leido', models.BooleanField()),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensajeentrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.CharField(blank=True, max_length=250, null=True)),
                ('enviado', models.DateField(auto_now_add=True)),
                ('leido', models.BooleanField()),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
