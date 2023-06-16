from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.


class ProfileModel(models.Model):
    username = models.CharField(max_length=10,
                                validators=[MinLengthValidator(2, message="The username must be a minimum of 2 chars")])
    email = models.EmailField()
    age = models.IntegerField(MinValueValidator(18))
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    profile_picture = models.URLField(null=True)
