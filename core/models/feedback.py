from django.db import models

class Feedback(models.Model):
	opiniao = models.TextField()
	estrelas = models.IntegerField()
	criado_em = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.estrelas} estrelas - {self.opiniao[:30]}"
