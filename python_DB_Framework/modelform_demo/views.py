from django.shortcuts import render, redirect
from .forms import RestaurantForm

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecting to same page with a success message flag
            return redirect('/session7/add/?success=1')
    else:
        form = RestaurantForm()
    
    success = request.GET.get('success', False)
    return render(request, 'modelform_demo/add_restaurant.html', {'form': form, 'success': success})
