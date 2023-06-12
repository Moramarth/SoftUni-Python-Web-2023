from django.contrib import admin

from Petstagram.common.models import Comment, Like


# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "date_time_of_publication", "to_photo"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["to_photo"]
