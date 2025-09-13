
from django.urls import path
from . import views

urlpatterns = [
    path("animes/", views.anime_list, name="anime_list"),
    path("animes/<int:pk>/", views.anime_detail, name="anime_detail"),
    path("animes/importar/", views.importar_animes_ajax, name="importar_animes_ajax"),
]
