from django import forms
from apps.catalogo.models.Product import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['status']