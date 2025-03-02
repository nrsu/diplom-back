from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Импортируем кастомную модель пользователя

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser  # Используем кастомную модель
        fields = ['username', 'email', 'password1', 'password2']
    

