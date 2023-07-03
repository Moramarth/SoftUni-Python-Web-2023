from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm
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


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')


class UserEditView(views.UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('show profile details', kwargs={"pk": self.object.pk})


class UserDeleteView(views.DeleteView):
    model = PetstagramUser
    template_name = 'accounts/profile-delete-page.html'
    next_page = reverse_lazy('home page')

    def post(self, *args, pk):
        self.request.user.delete()


class UserDetailsView(views.DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




