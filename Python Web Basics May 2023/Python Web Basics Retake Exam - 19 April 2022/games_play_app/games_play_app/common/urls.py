from django.urls import path

from .views import home_page, display_dashboard

urlpatterns = [
    path("", home_page, name="home page"),
    path("dashboard/", display_dashboard, name ="display dashboard")
]