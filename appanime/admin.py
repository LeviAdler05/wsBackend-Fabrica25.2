from django.contrib import admin
from .models import Anime, Quote, Genero

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano_lancamento", "status")
    filter_horizontal = ("generos",)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("anime", "personagem", "citacao")

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nome",)