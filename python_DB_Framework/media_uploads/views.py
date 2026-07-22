from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def upload_profile_view(request):
    if request.method == 'POST':
        # request.FILES must be passed to the form to handle the uploaded file
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
        
    return render(request, 'media_uploads/upload.html', {'form': form})

def profile_list_view(request):
    profiles = UserProfile.objects.all()
    return render(request, 'media_uploads/profile_list.html', {'profiles': profiles})
