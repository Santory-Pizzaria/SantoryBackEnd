from django.db import models


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

    
    def __str__(self):
        return f"{self.id} - {self.rua}, {self.numero} - {self.bairro}, {self.cidade} - {self.cep}"
