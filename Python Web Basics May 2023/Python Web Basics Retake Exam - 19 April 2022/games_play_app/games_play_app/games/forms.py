from django import forms

from games_play_app.games.models import Game


class GameForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Game.CATEGORY_CHOICES)

    class Meta:
        model = Game
        fields = "__all__"
        widgets = {
            "created_by": forms.HiddenInput(),
        }


class GameDeleteForm(GameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
