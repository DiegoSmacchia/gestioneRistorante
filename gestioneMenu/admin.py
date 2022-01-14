from django.contrib import admin
from .models import Categoria, Ingrediente, Menu, Piatto, Misura, IngredientePiatto

# Register your models here.
admin.site.register(Ingrediente)
admin.site.register(Piatto)
admin.site.register(Misura)
admin.site.register(IngredientePiatto)
admin.site.register(Categoria)
admin.site.register(Menu)