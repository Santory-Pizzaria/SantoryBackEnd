from django.db import models
from core.models.produto import Produto

class ItemPedido(models.Model):
    # usa referência por string para evitar import circular
    pedido = models.ForeignKey('core.Pedido', on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.id} - {self.produto.nome} - {self.quantidade} - {self.preco_unitario}"