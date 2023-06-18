from django import forms

from my_music_app.accounts.models import Profile


class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    age = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Age"}))

    class Meta:
        model = Profile
        fields = '__all__'
