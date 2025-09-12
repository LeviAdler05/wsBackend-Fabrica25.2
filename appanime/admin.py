from django.contrib import admin
from .models import Anime, Quote

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano_lancamento", "genero")

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("anime", "autor", "texto")
