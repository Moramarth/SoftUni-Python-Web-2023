from django.contrib import admin

from my_site.tasks.models import Task

# Register your models here.

admin.site.register(Task)