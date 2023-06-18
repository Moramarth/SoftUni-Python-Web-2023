from django.urls import path

from .views import profile_details

urlpatterns = [
    path("", profile_details, name="profile details")
]