from django import forms

from car_collection_app.cars.models import CarModel


class CarCreateForm(forms.ModelForm):
    car_type = forms.ChoiceField(choices=CarModel.CAR_CHOICES, label="Type")

    class Meta:
        model = CarModel
        fields = '__all__'
        widgets = {
            "belongs_to": forms.HiddenInput()
        }

        labels = {
            "image_url": "Image URL"
        }


class CarDeleteForm(CarCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["disabled"] = "disabled"
