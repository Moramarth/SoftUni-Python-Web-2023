from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.accounts.validators import only_letters_validator


# Create your models here.
class PetstagramUser(AbstractUser):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Do not show", "Do not show"),
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(2), only_letters_validator])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(2), only_letters_validator])
    profile_picture = models.URLField()
    gender = models.CharField(choices=GENDER_CHOICES)
