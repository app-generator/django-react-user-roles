from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    # Page from the theme
    return render(request, "pages/index.html")


@login_required(login_url='/accounts/login/')
def profile(request):
  context = {
    'segment': 'profile',
  }
  return render(request, 'pages/profile.html', context)
