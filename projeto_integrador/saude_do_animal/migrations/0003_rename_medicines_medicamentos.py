# Generated by Django 4.2 on 2023-05-09 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro_de_animal', '0008_delete_vacina'),
        ('saude_do_animal', '0002_medicines'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Medicines',
            new_name='Medicamentos',
        ),
    ]
