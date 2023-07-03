from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm
from petstagram.accounts.models import PetstagramUser


# Create your views here.

class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home page')


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')