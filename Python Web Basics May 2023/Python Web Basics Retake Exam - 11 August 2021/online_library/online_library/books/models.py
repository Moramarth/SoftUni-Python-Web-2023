from django.db import models

from online_library.accounts.models import Profile


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.URLField()
    book_type = models.CharField(max_length=30)
    belongs_to = models.ForeignKey(Profile, on_delete=models.CASCADE)
    