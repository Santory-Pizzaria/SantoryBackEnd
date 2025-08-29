from django.db import models

class Combo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.URLField(blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.preco}"
