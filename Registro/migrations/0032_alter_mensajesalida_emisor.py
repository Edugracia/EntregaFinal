# Generated by Django 4.1.3 on 2023-01-17 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registro', '0031_alter_mensajesalida_emisor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajesalida',
            name='emisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to=settings.AUTH_USER_MODEL),
        ),
    ]
