from django.urls import path, include
from .views import register_user, login_user, show_profile_details, edit_profile, delete_profile

urlpatterns = [
    path('register/', register_user, name="register user"),
    path('login/', login_user, name="login user"),
    path('profile/<int:pk>/', include([
        path('', show_profile_details, name="show profile details"),
        path('edit/', edit_profile, name="edit profile"),
        path('delete/', delete_profile, name="delete profile")
    ])),
]
