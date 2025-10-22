from django.db import models
from django.utils import timezone
from core.models.user import User
from core.models.carrinho import Carrinho

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('confirmado', 'Confirmado'),
        ('preparando', 'Preparando'),
        ('em_entrega', 'Em Entrega'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.JSONField(help_text='Lista de itens do pedido (pizzas, bebidas, etc)')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    # Endereço embutido para simplicidade
    cep = models.CharField(max_length=20, blank=True, null=True)
    rua = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=120, blank=True, null=True)
    uf = models.CharField(max_length=10, blank=True, null=True)

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='confirmado')
    pagamento_status = models.CharField(max_length=32, blank=True, default='pendente')
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    tempo_entrega_min = models.PositiveIntegerField(blank=True, null=True, help_text='Estimativa mínima em minutos')
    tempo_entrega_max = models.PositiveIntegerField(blank=True, null=True, help_text='Estimativa máxima em minutos')

    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario} - {self.status}"