from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Anime
from .utils import importar_animes

def anime_list(request):
    animes = Anime.objects.all()
    return render(request, "appanime/anime_list.html", {"animes": animes})

def anime_detail(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    return render(request, "appanime/anime_detail.html", {"anime": anime})

def importar_animes_ajax(request):
    query = request.GET.get("query", "naruto")
    limit = int(request.GET.get("limit", 5))
    salvos = importar_animes(query=query, limit=limit)
    return JsonResponse({"salvos": salvos, "total": len(salvos)})
