from django import forms
from django.contrib.auth.forms import User
from .models import animes
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class AnimeForm(forms.ModelForm):
    class Meta:
        model = animes
        fields = ['animes_name', 'animes_sypnosis', 'animes_status', 'animes_type', 'animes_release_year', 'animes_poster_url']