from django.core.validators import MinValueValidator
from django.db import models

from my_music_app.accounts.validators import username_validation


# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinValueValidator(2), username_validation])
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(0)])
