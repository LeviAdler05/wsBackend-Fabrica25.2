import requests
import time
from django.core.management.base import BaseCommand
from appanime.models import Anime, Genero

class Command(BaseCommand):
    help = 'Busca e salva animes da API Jikan.moe'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('🚀 Iniciando a busca por animes...'))

        for page in range(1, 6):
            self.stdout.write(self.style.HTTP_INFO(f'🔎 Buscando animes na página {page}...'))
            api_url = f'https://api.jikan.moe/v4/top/anime?page={page}'
            
            try:
                response = requests.get(api_url)
                response.raise_for_status()
                animes_data = response.json().get('data', [])

                if not animes_data:
                    self.stdout.write(self.style.WARNING('Nenhum anime encontrado nesta página. Finalizando.'))
                    break

                for anime_data in animes_data:
                    titulo_anime = anime_data.get('title', 'Título não encontrado')

                    anime, created = Anime.objects.update_or_create(
                        titulo=titulo_anime,
                        defaults={
                            'titulo_ingles': anime_data.get('title_english'),
                            'sinopse': anime_data.get('synopsis', 'Sem sinopse.'),
                            'imagem_url': anime_data.get('images', {}).get('jpg', {}).get('large_image_url'),
                            'episodios': anime_data.get('episodes'),
                            'status': anime_data.get('status'),
                            'ano_lancamento': anime_data.get('year'),
                        }
                    )

                    for genero_data in anime_data.get('genres', []):
                        genero, _ = Genero.objects.get_or_create(nome=genero_data['name'])
                        anime.generos.add(genero)

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'✅ Anime "{titulo_anime}" foi salvo!'))
                    else:
                        self.stdout.write(self.style.NOTICE(f'☑️ Anime "{titulo_anime}" já existia, dados atualizados.'))

                self.stdout.write(self.style.HTTP_INFO('⏸️ Pausando por 2 segundos para não sobrecarregar a API...'))
                time.sleep(2)

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f'❌ Erro ao conectar na API: {e}'))
                break
        
        self.stdout.write(self.style.SUCCESS('🎉 Processo de importação finalizado!'))