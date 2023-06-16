from django import forms

from my_plant_app.plants.models import Plant


class PlantForm(forms.ModelForm):

    plant_type = forms.ChoiceField(choices=Plant.TYPE_CHOICES, label="Type")

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
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
