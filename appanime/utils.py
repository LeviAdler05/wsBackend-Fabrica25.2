import requests

JIKAN_BASE_URL = "https://api.jikan.moe/v4/anime"

def buscar_anime_jikan(query, limit=5):
    """
    Busca animes no Jikan API pelo nome (query).
    Retorna uma lista de dicionários com os dados do anime.
    """
    url = f"{JIKAN_BASE_URL}?q={query}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # levanta erro se não for 200
        data = response.json()
        resultados = []

        for item in data.get("data", []):
            anime_info = {
                "nome": item.get("title"),
                "imagem_capa": item.get("images", {}).get("jpg", {}).get("image_url"),
                "ano_lancamento": item.get("aired", {}).get("from", None)[:4] if item.get("aired", {}).get("from") else None,
                "descricao": item.get("synopsis"),
                "genero": ", ".join([g["name"] for g in item.get("genres", [])])
            }
            resultados.append(anime_info)

        return resultados
    except Exception as e:
        print(f"Erro ao buscar anime no Jikan: {e}")
        return []
