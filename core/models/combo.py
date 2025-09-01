from django.db import models
from core.models.pizza import Pizza
from core.models.bebida import Bebida

class Combo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='combos/', blank=True, null=True)
    pizzas = models.ManyToManyField(Pizza, blank=True)
    bebidas = models.ManyToManyField(Bebida, blank=True)
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.preco}"
