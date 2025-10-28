from django.db import models
from core.models.user import User

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField()
    mesa = models.IntegerField(null=True, blank=True)
    quantidade_pessoas = models.PositiveIntegerField()
    horario = models.TimeField()

    def __str__(self):
        return f"Reserva de {self.usuario} - {self.data} - Mesa: {self.mesa} - Pessoas: {self.quantidade_pessoas}"