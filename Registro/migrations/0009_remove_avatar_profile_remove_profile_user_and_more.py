# Generated by Django 4.1.3 on 2023-01-12 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registro', '0008_remove_avatar_user_avatar_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='avatars'),
            preserve_default=False,
        ),
    ]
