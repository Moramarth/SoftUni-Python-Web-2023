from django.urls import path

from .views import profile_details, delete_profile

urlpatterns = [
    path("details/", profile_details, name="profile details"),
    path("delete/", delete_profile, name="delete profile"),
]