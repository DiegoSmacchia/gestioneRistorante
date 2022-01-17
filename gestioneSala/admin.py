from django.contrib import admin
from gestioneSala.models import ComponenteOrdine, Ordine, Sala, Stato, Tavolo, OrdineTemporaneo, ComponenteTemporaneo

# Register your models here.
admin.site.register(Sala)
admin.site.register(Tavolo)
admin.site.register(Stato)
admin.site.register(Ordine)
admin.site.register(ComponenteOrdine)
admin.site.register(OrdineTemporaneo)
admin.site.register(ComponenteTemporaneo)