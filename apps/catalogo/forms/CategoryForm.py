from django import forms
from apps.catalogo.models.Category import Category

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ['status']