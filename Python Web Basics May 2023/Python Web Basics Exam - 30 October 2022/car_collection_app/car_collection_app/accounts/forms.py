from django import forms

from car_collection_app.accounts.models import ProfileModel


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = ProfileModel
        exclude = ["first_name", "last_name", "profile_picture"]

        widgets = {
            "password": forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

