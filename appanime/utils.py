import requests
from .models import Anime, Quote

import certifi  # Para garantir que Requests encontre os certificados SSL

# -------------------- Jikan API --------------------
JIKAN_BASE_URL = "https://api.jikan.moe/v4/anime"

def importar_animes(query="naruto", limit=5):
    """
    Busca animes na API Jikan e salva no banco.
    """
    url = f"{JIKAN_BASE_URL}?q={query}&limit={limit}"
    try:
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()
        data = response.json()
        
        salvos = []
        for item in data.get("data", []):
            anime_obj, criado = Anime.objects.get_or_create(
                nome=item.get("title"),
                defaults={
                    "imagem": item.get("images", {}).get("jpg", {}).get("image_url"),
                    "ano": item.get("aired", {}).get("from", None)[:4] if item.get("aired", {}).get("from") else None,
                    "descricao": item.get("synopsis"),
                    "genero": ", ".join([g["name"] for g in item.get("genres", [])])
                }
            )
            if criado:
                salvos.append(anime_obj.nome)
        return salvos
    except Exception as e:
        print(f"Erro ao importar animes: {e}")
        return []
