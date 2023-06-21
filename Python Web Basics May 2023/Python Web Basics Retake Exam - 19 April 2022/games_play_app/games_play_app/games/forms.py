from django import forms

from games_play_app.games.models import Game


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = "__all__"
        widgets = {
            "created_by": forms.HiddenInput(),
        }


class GameDeleteForm(GameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["disabled"] = "disabled"

