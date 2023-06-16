from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(12)])
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
