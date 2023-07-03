from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from petstagram.accounts.models import PetstagramUser


class PetstagramUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PetstagramUser
        fields = ["username", "email"]


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs= {"autofocus": True, "placeholder": "Username"}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "placeholder": "Password"})
    )
