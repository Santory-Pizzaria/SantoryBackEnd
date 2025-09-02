from django.db import models
from core.models.user import User
from core.models.carrinho import Carrinho

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.SET_NULL, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.CharField(max_length=20, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    tempo_entrega = models.IntegerField(default=0)  # minutos

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.name} - {self.status} - {self.valor_total}"