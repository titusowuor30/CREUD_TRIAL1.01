from django import forms
from apps.product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('category','title','price')
        labels={
            'category': 'Product Category',
            'title': 'Product Title',
            'price': 'Standard price'
        }