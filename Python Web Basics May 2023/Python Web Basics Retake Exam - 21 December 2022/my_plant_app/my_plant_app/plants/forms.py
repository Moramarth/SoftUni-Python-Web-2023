from django import forms

from my_plant_app.plants.models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = [
            "plant_type", "name", "image_url", "description", "price", "belongs_to"
        ]
        widgets = {
            "belongs_to": forms.HiddenInput()
        }
        labels = {
            "image_url": "Image URL",
        }


class PlantDeleteForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["disabled"] = "disabled"
