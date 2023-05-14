from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Vacina(models.Model):
    vac_id = models.AutoField(primary_key=True)
    vac_nome = models.CharField(max_length=50)
    vac_data_admin = models.DateField()
    vac_num_dose = models.IntegerField()
    vac_fabricante = models.CharField(max_length=50)
    vac_validade = models.DateField()
    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE)

    def __str__(self):
        return self.vac_nome
