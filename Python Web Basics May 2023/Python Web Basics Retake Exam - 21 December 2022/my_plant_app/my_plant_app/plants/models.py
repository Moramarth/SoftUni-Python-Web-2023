from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.plants.validators import only_letters_validation


# Create your models here.


class Plant(models.Model):
    plant_type = models.CharField(max_length=14)
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), only_letters_validation])
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
