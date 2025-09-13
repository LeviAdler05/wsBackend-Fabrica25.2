import requests
from .models import Anime, Quote
import certifi

JIKAN_BASE_URL = "https://api.jikan.moe/v4/anime"
ANIMECHAN_BASE_URL = "https://animechan.vercel.app/api/quotes"

def buscar_anime_jikan(query, limit=5):
    url = f"{JIKAN_BASE_URL}?q={query}&limit={limit}"
    try:
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()
        data = response.json()
        resultados = []
        for item in data.get("data", []):
            anime_info = {
                "nome": item.get("title"),
                "imagem": item.get("images", {}).get("jpg", {}).get("image_url"),
                "ano": item.get("aired", {}).get("from", None)[:4] if item.get("aired", {}).get("from") else None,
                "descricao": item.get("synopsis"),
                "genero": ", ".join([g["name"] for g in item.get("genres", [])])
            }
            resultados.append(anime_info)
        return resultados
    except Exception as e:
        print(f"Erro ao buscar anime no Jikan: {e}")
        return []

def buscar_quotes_anime(anime_name, limit=5):
    url = f"{ANIMECHAN_BASE_URL}/character?title={anime_name}"
    quotes = []
    try:
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()
        data = response.json()
        for item in data[:limit]:
            quotes.append({
                "texto": item.get("quote"),
                "autor": item.get("character"),
                "anime": item.get("anime")
            })
        return quotes
    except Exception as e:
        print(f"Erro ao buscar quotes de {anime_name}: {e}")
        return []

def importar_animes(query="naruto", limit=5):
    resultados = buscar_anime_jikan(query, limit)
    salvos = []
    for anime_data in resultados:
        anime_obj, criado = Anime.objects.get_or_create(
            nome=anime_data["nome"],
            defaults=anime_data
        )
        if criado:
            salvos.append(anime_obj.nome)
        quotes = buscar_quotes_anime(anime_data["nome"], limit=5)
        for q in quotes:
            if not Quote.objects.filter(anime=anime_obj, texto=q["texto"]).exists():
                Quote.objects.create(
                    anime=anime_obj,
                    texto=q["texto"],
                    autor=q["autor"]
                )
    return salvos
