# Generated by Django 5.1.6 on 2025-03-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_photo',
            name='users_photo_url',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='photo_perfil/', verbose_name='Foto de perfil del usuario'),
        ),
    ]
