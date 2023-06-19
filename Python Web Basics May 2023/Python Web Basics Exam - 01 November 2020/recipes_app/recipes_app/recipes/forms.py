from django import forms

from recipes_app.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

        labels = {
            "time": "Time(Minutes)",
            "image_url": "Image URL",
        }


class RecipeDeleteForm(RecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["readonly"] = ["readonly"]
            field.widget.attrs["disabled"] = ["disabled"]
