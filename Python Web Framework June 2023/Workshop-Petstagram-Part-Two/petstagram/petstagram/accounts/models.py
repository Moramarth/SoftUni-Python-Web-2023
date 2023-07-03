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
    first_name = models.CharField(max_length=30, blank=True, null=True,
                                  validators=[MinLengthValidator(2), only_letters_validator])
    last_name = models.CharField(max_length=30, blank=True, null=True,
                                 validators=[MinLengthValidator(2), only_letters_validator])
    profile_picture = models.URLField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, blank=True, max_length=11, default="Do not show")

    def get_user_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username
