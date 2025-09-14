from rest_framework import serializers
from .models import Anime, Quote, Genero

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class AnimeSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(many=True, read_only=True)
    quotes = QuoteSerializer(many=True, read_only=True)

    class Meta:
        model = Anime
        fields = '__all__'