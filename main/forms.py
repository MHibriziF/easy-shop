from django.forms import ModelForm
from main.models import Product
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-64 py-2 px-4 border border-gray-300 rounded-md',
        'placeholder': 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-64 mt-2 py-2 px-4 border border-gray-300 rounded-md',
        'placeholder': 'Password'
    }))