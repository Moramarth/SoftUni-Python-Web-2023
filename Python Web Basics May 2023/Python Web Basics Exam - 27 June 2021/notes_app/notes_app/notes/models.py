from django.db import models

from notes_app.accounts.models import Profile


# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image_url = models.URLField()
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
