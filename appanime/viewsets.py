from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Anime, Quote
from .serializers import AnimeSerializer, QuoteSerializer
from .utils import buscar_anime_jikan

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    @action(detail=False, methods=["post"])
    def importar(self, request):
        query = request.data.get("query")
        limit = int(request.data.get("limit", 5))
        if not query:
            return Response({"error": "É necessário informar o campo 'query'."}, status=400)
        resultados = buscar_anime_jikan(query, limit)
        salvos = []
        for anime_data in resultados:
            anime_obj, criado = Anime.objects.get_or_create(
                nome=anime_data["nome"],
                defaults=anime_data
            )
            if criado:
                salvos.append(anime_obj.nome)
        return Response({"salvos": salvos, "total": len(salvos)})

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
