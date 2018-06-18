from django.contrib import admin
from .models import Membre, Activite, Tarif, Cotisation


@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Activite)
admin.site.register(Tarif)

