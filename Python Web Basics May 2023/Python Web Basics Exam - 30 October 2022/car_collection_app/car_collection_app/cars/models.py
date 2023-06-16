from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection_app.accounts.models import ProfileModel
from car_collection_app.cars.validators import year_range_validation


# Create your models here.


class CarModel(models.Model):
    CAR_CHOICES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )
    car_type = models.CharField(max_length=10, choices=CAR_CHOICES)
    model = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField(validators=[year_range_validation])
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(1)])
    belongs_to = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
