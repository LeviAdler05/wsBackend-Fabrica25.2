from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Anime, Quote
from .serializers import AnimeSerializer, QuoteSerializer
from .utils import importar_animes  # ← Importando a função corrigida

class AnimeViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o CRUD de Animes.
    """
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    @action(detail=False, methods=["post"])
    def importar(self, request):
        """
        Busca animes na API Jikan e salva no banco.
        Recebe um JSON com {"query": "nome do anime", "limit": 5}
        """
        query = request.data.get("query")
        limit = int(request.data.get("limit", 5))
        if not query:
            return Response({"error": "É necessário informar o campo 'query'."}, status=400)

        salvos = importar_animes(query=query, limit=limit)  # Função que busca e salva no banco
        return Response({"salvos": salvos, "total": len(salvos)})


class QuoteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o CRUD de Quotes.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
