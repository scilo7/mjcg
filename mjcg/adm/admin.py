from django.contrib import admin
from .models import Membre, Activite, Tarif, Cotisation


admin.site.register(Activite)
# admin.site.register(Cotisation)


class CotisationInline(admin.TabularInline):
    model = Cotisation
    extra = 0


@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    
    list_filter = ('annee',)


@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    
    inlines = [
        CotisationInline,
    ]