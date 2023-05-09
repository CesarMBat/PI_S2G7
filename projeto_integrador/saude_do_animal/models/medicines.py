from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Medicamentos(models.Model):
    med_id = models.AutoField(primary_key=True)
    med_nome = models.CharField(max_length=50)
    med_dosagem = models.CharField(max_length=50)
    med_freq_admin = models.CharField(max_length=50)
    med_duracao = models.CharField(max_length=50)
    med_motivo_uso = models.CharField(max_length=150)
    animal_id = models.ForeignKey('registro_de_animal.animal', on_delete=models.CASCADE)

    def __str__(self):
        return self.med_nome
