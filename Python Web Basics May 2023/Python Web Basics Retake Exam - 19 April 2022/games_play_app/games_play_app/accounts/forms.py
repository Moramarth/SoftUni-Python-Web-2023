from django import forms

from games_play_app.accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "age", "password"]

        widgets = {
            "password": forms.PasswordInput()
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
