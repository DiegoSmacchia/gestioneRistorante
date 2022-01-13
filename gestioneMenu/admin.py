from django.contrib import admin
from .models import Ingrediente, Piatto, Misura, IngredientePiatto

# Register your models here.
admin.site.register(Ingrediente)
admin.site.register(Piatto)
admin.site.register(Misura)
admin.site.register(IngredientePiatto)