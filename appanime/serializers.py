from rest_framework import serializers
from .models import Anime, Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"

class AnimeSerializer(serializers.ModelSerializer):
    quotes = QuoteSerializer(many=True, read_only=True)
    class Meta:
        model = Anime
        fields = "__all__"
