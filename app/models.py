from django.db import models

# Create your models here. ONDE ESTÁ A REGRA DE NEGÓCIO DO NOSSO BANCO DE DADOS.
class ToDo(models.Model):
    activate = models.CharField(max_length=120)
    status = models.BooleanField(default=False)