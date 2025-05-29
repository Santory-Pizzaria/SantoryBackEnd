from django.db import models

class Usuario(models.Model):
    TIPOS = [
        ('administrador', 'Administrador'),
        ('atendente', 'Atendente'),
        ('pizzaiolo', 'Pizzaiolo'),
        ('entregador', 'Entregador'),
        ('cliente', 'Cliente'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.tipo}"