from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    curso = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=12, unique=True)
    data_ingresso = models.DateField()
    foto_aluno = models.ImageField(upload_to='alunos/')

    def __str__(self):
        return self.nome

