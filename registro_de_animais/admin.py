from django.contrib import admin

# Register your models here.
from .models.animais import *
from .models.vacinas import *

admin.site.register(Animal)

admin.site.register(Vacina)
