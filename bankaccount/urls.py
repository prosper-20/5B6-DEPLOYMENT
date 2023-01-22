from django.urls import path
from .views import real_home_page

urlpatterns = [
    path("", real_home_page, name="home-page")
]