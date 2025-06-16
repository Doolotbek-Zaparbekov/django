from django import forms
from .models import Basket

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['full_name', 'phone', 'card_number', 'book', 'status']
