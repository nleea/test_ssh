from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Archivos, Destinatarios


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["title", "description"]

class ArchivosForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = ['descripcion']

class ArchivosForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = ['descripcion']
