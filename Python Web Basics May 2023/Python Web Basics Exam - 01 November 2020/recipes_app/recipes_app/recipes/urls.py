from django.urls import path

from .views import home_page, create_recipe, edit_recipe, delete_recipe, recipe_details

urlpatterns = [
    path("", home_page, name="home page"),
    path("create/", create_recipe, name="create recipe"),
    path("edit/<int:pk>/", edit_recipe, name="edit recipe"),
    path("delete/<int:pk>/", delete_recipe, name="delete recipe"),
    path("details/<int:pk>/", recipe_details, name="recipe details"),
]