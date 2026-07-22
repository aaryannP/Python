from django.shortcuts import render, redirect
from .forms import AddRestaurantForm

def add_restaurant(request):
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            # In a real app we'd save to DB here, but this is a Form (not ModelForm)
            # We'll just pass data to session to show on success page
            request.session['submitted_data'] = form.cleaned_data
            return redirect('success_page')
    else:
        form = AddRestaurantForm()
    
    return render(request, 'forms_demo/add_restaurant.html', {'form': form})

def success_page(request):
    data = request.session.get('submitted_data', None)
    return render(request, 'forms_demo/success.html', {'data': data})
