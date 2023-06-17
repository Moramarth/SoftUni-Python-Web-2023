from django import forms

from my_music_app.albums.models import Album


class AlbumForm(forms.ModelForm):

    genre = forms.ChoiceField(choices=Album.GENRE_CHOICES)

    class Meta:
        model = Album
        fields = "__all__"

        widgets = {
            "created_by": forms.HiddenInput
        }
        labels = {
            "image_url": "Image URL"
        }


class AlbumDeleteForm(AlbumForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
