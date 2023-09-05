# Create your models here.
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    periodo_ingresso = models.DateField()
    notaweb_avancado = models.IntegerField()
    situacao = models.CharField(max_length=20)


class PaginaInicial(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()



# class Aluno(models.Model):
#     matricula = models.AutoField(primary_key=True)
#     nome = models.CharField(max_length=200)
#     periodo_ingresso = models.DateField()
#     notaweb_avancado = models.IntegerField()
#     situacao = models.CharField(max_length=20)
