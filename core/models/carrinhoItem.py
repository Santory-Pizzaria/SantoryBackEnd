from django.db import models
from core.models.carrinho import Carrinho

class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto_tipo = models.CharField(max_length=20)  # 'pizza', 'bebida', 'combo'
    produto_id = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto_tipo} (ID: {self.produto_id})"