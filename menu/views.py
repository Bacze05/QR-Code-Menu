from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria, Plato

class ConfigMenu(LoginRequiredMixin, View):
    model_categoria = Categoria
    model_plato = Plato
    template_name = 'base.html'

    def get_queryset_categorias(self):
        return self.model_categoria.objects.all().order_by('orden')  # Ordenar por el campo 'orden'

    def get_queryset_platos(self):
        return self.model_plato.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        categorias = self.get_queryset_categorias()
        platos = self.get_queryset_platos()
        context["categorias"] = categorias
        context["platos"] = platos
        return context
    
    def get(self, request, *args, **kwargs):  
        return render(request, self.template_name, self.get_context_data())



