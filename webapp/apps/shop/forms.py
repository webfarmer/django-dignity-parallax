from django import forms
from apps.shop.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['cart']


class ProductForm(forms.Form):
    product_item_id = forms.IntegerField()