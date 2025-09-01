from django.db import models

class Bebida(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='bebidas/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.preco}"