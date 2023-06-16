from django.urls import path

from .views import create_game, game_details, edit_game, delete_game

urlpatterns = [
    path("create/", create_game, name="create game"),
    path("details/<int:pk>/", game_details, name="game details"),
    path("edit/<int:pk>/", edit_game, name="edit game"),
    path("delete/<int:pk>/", delete_game, name="delete game"),
]