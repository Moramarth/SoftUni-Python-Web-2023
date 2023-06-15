from django.urls import path

from .views import create_plant, display_catalogue, plant_details, edit_plant, delete_plant

urlpatterns = [
    path("create/", create_plant, name='create plant'),
    path("catalogue/", display_catalogue, name="catalogue"),
    path("details/<int:pk>", plant_details, name="plant details"),
    path("edit/<int:pk>", edit_plant, name="edit plant"),
    path("delete/<int:pk>", delete_plant, name="delete plant"),

]