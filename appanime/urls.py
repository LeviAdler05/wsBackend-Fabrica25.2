from django.urls import path
from . import views

urlpatterns = [
    path("animes/", views.anime_list, name="anime_list"),
    path("animes/<int:pk>/", views.anime_detail, name="anime_detail"),
    path("importar/", views.importar_animes_view, name="importar_animes"),
]
