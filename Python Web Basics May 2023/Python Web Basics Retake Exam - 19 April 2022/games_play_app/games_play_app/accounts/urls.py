from django.urls import path

from .views import create_profile, profile_details, edit_profile, delete_profile

urlpatterns = [
    path("create/", create_profile, name="create profile"),
    path("details/", profile_details, name="profile details"),
    path("edit/", edit_profile, name="edit profile"),
    path("delete/", delete_profile, name="delete profile"),
]