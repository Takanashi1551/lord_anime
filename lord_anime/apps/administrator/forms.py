from django import forms
from django.contrib.auth.forms import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
