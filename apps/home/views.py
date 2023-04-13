from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

from allauth.socialaccount.models import SocialAccount

from apps.home.forms import UserProfileForm, LoginForm
from apps.home.models import UserProfile

# Create your views here.

def index(request):
    # Page from the theme
    return render(request, "pages/index.html")

@login_required(login_url="/accounts/login/")
def profile(request):
    user = get_object_or_404(User, username=request.user)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # Social Account
    social_account = {}
    social = SocialAccount.objects.filter(user=user.pk)
    if social.exists():
        social_account = social.first()

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            if request.POST.get('email'):
                user.email = request.POST.get('email')
                user.save()
            messages.success(request, "Profile updated successfully!")
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
        'social_account': social_account
    }
    return render(request, 'pages/profile.html', context)

class UserLoginView(LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm

  def get_context_data(self, *args, **kwargs):
      context = super(UserLoginView, self).get_context_data(*args, **kwargs)
      context['github_auth'] = getattr(settings, 'GITHUB_AUTH')
      context['twitter_auth'] = getattr(settings, 'TWITTER_AUTH')
      return context