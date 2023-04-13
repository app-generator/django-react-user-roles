from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("accounts/login/", views.UserLoginView.as_view(), name="login"),
    path('social_login/', include('allauth.urls'))
]
