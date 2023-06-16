from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from games_play_app.accounts.models import Profile


# Create your models here.


class Game(models.Model):
    CATEGORY_CHOICES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )

    title = models.CharField(max_length=30, unique=True)
    category = models.CharField(choices=CATEGORY_CHOICES)
    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])
    max_level = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    image_url = models.URLField()
    summary = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
