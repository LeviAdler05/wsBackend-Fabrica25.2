from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appanime.viewsets import AnimeViewSet, QuoteViewSet
from appanime import views

router = DefaultRouter()
router.register(r"animes", AnimeViewSet, basename="anime")
router.register(r"quotes", QuoteViewSet, basename="quote")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("animes/", views.anime_list, name="anime_list"),
    path("animes/<int:pk>/", views.anime_detail, name="anime_detail"),
    path("importar-animes/", views.importar_animes_ajax, name="importar_animes_ajax"),
]
