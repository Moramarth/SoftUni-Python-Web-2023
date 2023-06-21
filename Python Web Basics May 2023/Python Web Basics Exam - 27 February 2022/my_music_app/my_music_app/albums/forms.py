from django import forms

from my_music_app.albums.models import Album


class AlbumForm(forms.ModelForm):
    album_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Album Name"}))
    artist = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Artist"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Description"}))
    image_url = forms.CharField(label="Image URL", widget=forms.TextInput(attrs={"placeholder": "Image URL"}))
    price = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Price"}))

    class Meta:
        model = Album
        fields = "__all__"

        widgets = {
            "created_by": forms.HiddenInput()
        }


class AlbumDeleteForm(AlbumForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["disabled"] = "disabled"
