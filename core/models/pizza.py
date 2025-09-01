from django.db import models

class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    sabores = models.CharField(max_length=200)
    
def __str__(self):
        return f"{self.id} - {self.nome} - {self.preco}"