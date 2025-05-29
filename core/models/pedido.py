from django.db import models
from core.models.usuario import Usuario
from core.models.endereco import Endereco

class Pedido(models.Model):
    STATUS = [
        ('em preparo', 'Em Preparo'),
        ('em entrega', 'Em Entrega'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome} - {self.status} - {self.valor_total}"