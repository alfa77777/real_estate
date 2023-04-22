from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages import get_messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, CreateView

from account.forms import CustomAuthenticationForm, RegistrationForm
from houses.models import House


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "account/login.html"


# @login_required()
def custom_login(request):
    form = CustomAuthenticationForm(request.POST or None)
    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password:
            user = authenticate(
                request, username=username, password=password
            )
            login(request, user)
            return redirect("account:profile")
    return render(request, "account/login.html", {"form": form})

#
# class UserProfile(DetailView):
#     model = User
#     pk_url_kwarg = None
#     query_pk_and_slug = None
#
#     def get_queryset(self):
#         return self.request.user

def profile(request):
    if request.user.is_authenticated:
        return render(request, "account/profile.html", {"user": request.user})
    return redirect("account:login")


class RegisterView(CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect("homepage")
        return render(request, "account/register.html", {"form": form, 'messages': get_messages(request)})


# class SearchView(ListView):
#     queryset = House.objects.all()
#     template_name = "search.html"
#     context_object_name = "results"
#
#
def search(request):
    search_query = request.POST.get("search")
    expression = Q(address__icontains=search_query) | \
                 Q(country__name__icontains=search_query)
    queryset = House.objects.filter(expression)
    return render(request, "search.html", {"results": queryset})

# def login(request):
#     form = CustomAuthenticationForm()
#     return render(request, "account/login.html", {"form": form})


# class AccountSignupView(LoginView):
#     form_class = CustomAuthenticationForm
#     template_name = "account/sign_up.html"

# class AccountSignupView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'account/sign_up.html'

