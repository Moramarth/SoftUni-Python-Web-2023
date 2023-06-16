from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.accounts.models import Profile
from my_plant_app.plants.validators import only_letters_validation


# Create your models here.


class Plant(models.Model):
    TYPE_CHOICES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )
    plant_type = models.CharField(max_length=14, choices=TYPE_CHOICES)
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_validation])
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    belongs_to = models.ForeignKey(Profile, on_delete=models.CASCADE)
