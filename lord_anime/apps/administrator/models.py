from django.db import models

# Create your models here.
class animes(models.Model):
    animes_name = models.CharField('Nombre del anime', max_length=240, null=True, blank=True)
    animes_sypnosis = models.TextField('Sinopsis del anime', max_length=2000, null=True, blank=True)
    animes_status = models.BooleanField('Estado del anime', default=False)
    animes_type = models.CharField('Tipo de anime', max_length=240, null=True, blank=True)
    animes_chapters = models.IntegerField('Capitulos del anime', null=True, blank=True)
    animes_release_year = models.DateField('Fecha de lanzamiento del anime', null=True, blank=True)
    animes_poster_url = models.ImageField('Imagen del anime', max_length=200, upload_to='posters/', height_field=None, width_field=None, null=True, blank=True)
# foreign key genders
    animes_genders = models.ManyToManyField('animes_genders', related_name='animes', blank=True)

# Name of the table in the database
    class Meta:
        db_table = 'anime'

    def __str__(self):
        return self.animes_name

class animes_genders(models.Model):
    animes_genders_name = models.CharField('Genero del anime', max_length=240, null=True, blank=True)

# Name of the table in the database
    class Meta:
        db_table = 'anime_genders'

    def __str__(self):
        return self.animes_genders_name