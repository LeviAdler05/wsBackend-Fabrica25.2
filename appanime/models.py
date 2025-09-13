from django.db import models

class Anime(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.URLField(blank=True, null=True)
    ano = models.CharField(max_length=10, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    genero = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome

class Quote(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name="quotes")
    texto = models.TextField()
    autor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.texto} - {self.autor or 'Desconhecido'}"
