from django import forms
from django.core.validators import MinLengthValidator

class AddRestaurantForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        validators=[MinLengthValidator(3)],
        label='Restaurant Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'})
    )
    cuisine = forms.CharField(
        max_length=50,
        label='Cuisine Type',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cuisine'})
    )
    email = forms.EmailField(
        label='Contact Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )
