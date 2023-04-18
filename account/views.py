from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from account.forms import CustomAuthenticationForm


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "account/login.html"


# class AccountSignupView(LoginView):
#     form_class = CustomAuthenticationForm
#     template_name = "account/sign_up.html"

class AccountSignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/sign_up.html'

