from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import RegisterView, custom_login, profile, search

app_name = "account"

urlpatterns = [
    path("login/", custom_login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
    path("sign_up/", RegisterView.as_view(), name="register"),
    path("search/", search, name="search")
]
