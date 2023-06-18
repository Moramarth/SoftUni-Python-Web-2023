from django import forms

from notes_app.accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        labels = {
            "image_url": "Link to Profile Image"
        }
