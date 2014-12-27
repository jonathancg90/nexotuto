from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from apps.catalogo.models.Product import Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        exclude = ['status']
