from django.db import models
from core.models.endereco import Endereco

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email}"