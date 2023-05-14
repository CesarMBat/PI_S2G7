from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Animal(models.Model):
    tutor = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)
    cor = models.CharField(max_length=50)
    foto = models.ImageField()
    porte = models.CharField(max_length=50)
    raça = models.CharField(max_length=50)
    rga = models.CharField(max_length=50)
    castrado = models.BooleanField()
    anilha = models.CharField(max_length=50)
    chip = models.CharField(max_length=50)
    vacinado = models.BooleanField()
    vermifugado = models.BooleanField()

    def __str__(self):
        return self.name