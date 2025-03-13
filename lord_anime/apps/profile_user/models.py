from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class users_photo(models.Model):
    users_photo_url = models.ImageField('Foto de perfil del usuario',max_length=200, upload_to='photo_perfil/', height_field=None, width_field=None , null=True, blank=True)
    fk_users_aut_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.fk_users_aut_user)