from django.urls import path, include
from .views import UserRegisterView, UserLoginView, UserLogoutView, show_profile_details, edit_profile, delete_profile

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register user"),
    path('login/', UserLoginView.as_view(), name="login user"),
    path('logout/', UserLogoutView.as_view(), name="logout user"),
    path('profile/<int:pk>/', include([
        path('', show_profile_details, name="show profile details"),
        path('edit/', edit_profile, name="edit profile"),
        path('delete/', delete_profile, name="delete profile")
    ])),
]
