import requests
import time
import random
from django.core.management.base import BaseCommand
from appanime.models import Anime, Quote
from urllib.parse import quote as url_quote
from requests.exceptions import HTTPError

class Command(BaseCommand):
    help = 'Busca e salva citações de animes da API AnimeChan'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('🚀 Iniciando a busca por citações para 10 animes aleatórios...'))

        animes_no_banco = list(Anime.objects.all())
        if not animes_no_banco:
            self.stdout.write(self.style.WARNING('Nenhum anime encontrado no banco de dados. Rode o comando "import_animes" primeiro.'))
            return
        
        animes_selecionados = random.sample(animes_no_banco, min(len(animes_no_banco), 10))

        for anime in animes_selecionados:
            nome_para_busca = anime.titulo_ingles or anime.titulo
            nome_formatado = url_quote(nome_para_busca)
            api_url = f'https://animechan.xyz/api/quotes/anime?title={nome_formatado}'
            
            self.stdout.write(self.style.HTTP_INFO(f'🔎 Buscando citações para "{nome_para_busca}"...'))

            try:
                response = requests.get(api_url)
                response.raise_for_status()
                quotes_data = response.json()

                for quote_data in quotes_data:
                    quote_obj, created = Quote.objects.get_or_create(
                        anime=anime,
                        citacao=quote_data['quote'],
                        defaults={'personagem': quote_data['character']}
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'✅ Citação de "{quote_data["character"]}" salva!'))
                
                self.stdout.write(self.style.HTTP_INFO('⏸️ Pausando por 5 segundos...'))
                time.sleep(5)

            except HTTPError as http_err:
                if http_err.response.status_code == 429:
                    self.stdout.write(self.style.WARNING('❕ Rate limit atingido. Pausando por 30 segundos...'))
                    time.sleep(30)
                else:
                    self.stdout.write(self.style.ERROR(f'❌ Erro HTTP para "{nome_para_busca}": {http_err}'))
            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f'❌ Erro de conexão para "{nome_para_busca}": {e}'))
                time.sleep(5)
        
        self.stdout.write(self.style.SUCCESS('🎉 Processo de importação de citações finalizado!'))