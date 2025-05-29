from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=30)
    estoque_atual = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.categoria} - {self.preco}"
