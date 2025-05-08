from django import forms 
from .models import *

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class ProductForm(forms.ModelForm):
    name =forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    quantity=forms.IntegerField(widget=forms.NumberInput(attrs={'autofocus':True,'class':'form-control'}))
    
    class Meta:
        model = Product
        fields=['name','category','quantity','cost_per_item','quantity_sold']
    
    cost_per_item=forms.DecimalField(required=True)
    quantity_sold=forms.IntegerField(required=True)

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['product','order_quantity']
# class ProductForm(Product):
#     name =forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
#     quantity=forms.IntegerField(widget=forms.NumberInput(attrs={'autofocus':True,'class':'form-control'}))
#     category = forms.CharField()
#     class Meta:
#         model = Product
#         fields=['name','category','quantity']