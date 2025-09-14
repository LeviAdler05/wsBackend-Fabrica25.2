from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appanime.viewsets import AnimeViewSet, QuoteViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'animes', AnimeViewSet, basename='anime-api')
router.register(r'quotes', QuoteViewSet, basename='quote-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('appanime.urls', namespace='appanime')),
]