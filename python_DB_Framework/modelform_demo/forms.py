from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter restaurant name', 'class': 'form-control'}),
            'cuisine': forms.TextInput(attrs={'placeholder': 'Enter cuisine type', 'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'})
        }
