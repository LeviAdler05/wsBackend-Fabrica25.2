import requests
import os
import django
import time

# Configura o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetoanime.settings")
django.setup()

from appanime.models import Anime

def importar_todos_animes(batch_size=50, delay=1):
    """
    Importa todos os animes da API Jikan, em lotes de 'batch_size',
    com pausa 'delay' entre requisições para não sobrecarregar a API.
    """
    base_url = "https://api.jikan.moe/v4/anime"
    page = 1
    total_importados = 0

    while True:
        try:
            response = requests.get(base_url, params={"limit": batch_size, "page": page}, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro na API na página {page}: {e}. Tentando novamente em 5s...")
            time.sleep(5)
            continue

        data = response.json().get("data", [])
        if not data:
            print("Nenhum anime encontrado nesta página. Importação finalizada.")
            break

        for item in data:
            title = item.get("title")
            year = item.get("year") or (item.get("aired", {}).get("from") or "")[:4]
            synopsis = item.get("synopsis")
            image_url = item.get("images", {}).get("jpg", {}).get("image_url")

            anime, criado = Anime.objects.get_or_create(
                title=title,
                defaults={
                    "year": year,
                    "synopsis": synopsis,
                    "image_url": image_url
                }
            )
            if criado:
                total_importados += 1
                print(f"Importado: {title}")

        page += 1
        print(f"Página {page-1} concluída. Total importados até agora: {total_importados}")
        time.sleep(delay)

    print(f"\nImportação completa! Total de animes importados: {total_importados}")


if __name__ == "__main__":
    importar_todos_animes(batch_size=50, delay=1)
