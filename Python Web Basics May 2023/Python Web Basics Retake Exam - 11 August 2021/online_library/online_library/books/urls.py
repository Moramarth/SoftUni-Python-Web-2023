from django.urls import path

from .views import add_book, book_details, edit_book

urlpatterns = [
    path("add/", add_book, name="add book"),
    path("edit/<int:pk>", edit_book, name="edit book"),
    path("details/<int:pk>/", book_details, name="book details"),
]