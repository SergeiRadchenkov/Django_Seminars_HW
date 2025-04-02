from django import forms
from .models import Client, Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model =Product
        fields = ['name', 'description', 'price', 'quantity', 'image']
