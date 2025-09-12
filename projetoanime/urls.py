from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appanime.viewsets import AnimeViewSet, QuoteViewSet

# Registrando os endpoints da API
router = DefaultRouter()
router.register(r"animes", AnimeViewSet, basename="anime")
router.register(r"quotes", QuoteViewSet, basename="quote")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # Endpoints da API
]
