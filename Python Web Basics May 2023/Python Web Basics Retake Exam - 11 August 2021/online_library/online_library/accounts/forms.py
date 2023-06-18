from django import forms

from online_library.accounts.models import Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    image_url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "URL"}))

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileDeleteForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["readonly"] = "readonly"
            field.widget.attrs["disabled"] = "disabled"


