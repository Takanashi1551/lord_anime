from django.db import models

# Create your models here.
class animes(models.Model):
    animes_name = models.CharField('Nombre del anime', max_length=240, null=True, blank=True)
    animes_sypnosis = models.TextField('Sinopsis del anime', max_length=2000, null=True, blank=True)
    animes_status = models.BooleanField('Estado del anime', default=False)
    animes_type = models.CharField('Tipo de anime', max_length=240, null=True, blank=True)
    animes_chapters = models.IntegerField('Capitulos del anime', null=True, blank=True)
    animes_release_year = models.DateField('Fecha de lanzamiento del anime', null=True, blank=True)
    animes_poster = models.ImageField('Imagen del anime', max_length=200, upload_to='animes_poster/', height_field=None, width_field=None, null=True, blank=True)

    def __str__(self):
        return self.animes_name

class animes_genders(models.Model):
    animes_genders_name = models.CharField('Genero del anime', max_length=240, null=True, blank=True)

    def __str__(self):
        return self.animes_genders_name

class gender_list(models.Model):
    fk_gender_list_anime = models.ForeignKey(animes, on_delete=models.CASCADE, null=True, blank=True)
    fk_gender_list_animes_genders = models.ForeignKey(animes_genders, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.fk_gender_list_anime} - {self.fk_gender_list_animes_genders}'