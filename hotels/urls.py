from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/<str:keyword>", views.search, name="search"),
    path("search_form", views.search_form, name="search_form"),
    path("rooms/<str:hotel_id>", views.find_rooms, name="rooms"),
    path("attractions", views.attractions, name="attractions"),
    path("prices", views.prices, name="prices"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
