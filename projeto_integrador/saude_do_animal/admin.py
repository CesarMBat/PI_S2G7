from django.contrib import admin

from .models.vaccines import *
from .models.medicines import *

admin.site.register(Vacina)
admin.site.register(Medicamentos)