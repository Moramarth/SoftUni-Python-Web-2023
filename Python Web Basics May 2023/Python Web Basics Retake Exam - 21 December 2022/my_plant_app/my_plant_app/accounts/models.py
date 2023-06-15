from django.core.validators import MinLengthValidator
from django.db import models


from my_plant_app.accounts.validators import first_letter_validation


# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    first_name = models.CharField(max_length=20, validators=[first_letter_validation])
    last_name = models.CharField(max_length=20, validators=[first_letter_validation])
    profile_picture = models.URLField(null=True)
