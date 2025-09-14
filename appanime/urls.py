from django.urls import path
from . import views

app_name = 'appanime'

urlpatterns = [
    path('', views.anime_list, name='anime_list'),
    path('animes/<int:pk>/', views.anime_detail, name='anime_detail'),
    path('animes/novo/', views.anime_create, name='anime_create'),
    path('animes/<int:pk>/editar/', views.anime_update, name='anime_update'),
    path('animes/<int:pk>/deletar/', views.anime_delete, name='anime_delete'),
]