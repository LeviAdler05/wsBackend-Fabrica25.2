from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Anime(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_ingles = models.CharField(max_length=255, blank=True, null=True)
    sinopse = models.TextField(blank=True, null=True)
    imagem_url = models.URLField(max_length=500, blank=True, null=True)
    episodios = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    ano_lancamento = models.IntegerField(blank=True, null=True)
    generos = models.ManyToManyField(Genero, blank=True)

    def __str__(self):
        return self.titulo

class Quote(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='quotes')
    personagem = models.CharField(max_length=255)
    citacao = models.TextField()

    def __str__(self):
        return f'"{self.citacao}" - {self.personagem}'