from django.contrib import admin

from petstagram.accounts.models import PetstagramUser


# Register your models here.

@admin.register(PetstagramUser)
class PetstagramUserAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "gender"]
