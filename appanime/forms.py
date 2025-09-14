from django import forms
from .models import Anime, Quote

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['titulo', 'titulo_ingles', 'sinopse', 'imagem_url', 'episodios', 'status', 'ano_lancamento', 'generos']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['anime', 'personagem', 'citacao']