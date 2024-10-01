from django.forms import ModelForm
from main.models import Product
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock"]
