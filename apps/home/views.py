from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from apps.home.forms import UserProfileForm
from apps.home.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    # Page from the theme
    return render(request, "pages/index.html")

@login_required(login_url="/accounts/login/")
def profile(request):
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form
    }
    return render(request, 'pages/profile.html', context)