from django.contrib import admin
from .models import *
# Register your models here.

class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')

admin.site.register(Plato, PlatoAdmin)
admin.site.register(Categoria)


