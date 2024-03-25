from django.db import models


class Acessorio(models.Model):
    descrição = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} ({self.id})'