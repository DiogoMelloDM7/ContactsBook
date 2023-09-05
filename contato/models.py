from django.db import models

# Create your models here.


class Contato(models.Model):

    telefone = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome
