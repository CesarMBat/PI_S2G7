from django.contrib import admin
from .models.animals import *
from .models.vaccines import *

admin.site.register(Tutor)
admin.site.register(Especie)
admin.site.register(Sexo)
admin.site.register(Porte)
admin.site.register(Raça)
admin.site.register(Animal)

admin.site.register(Vacina)