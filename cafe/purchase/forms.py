from django import forms
from .models import Inventory, Purchase

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['inventory_category', 'purchase', 'item', 'quantity', 'unit', 'shelf_number', 'expiry_date', 'price']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['category', 'item', 'unit', 'quantity', 'expiry_date', 'price']
