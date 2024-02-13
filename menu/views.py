from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic import TemplateView,ListView,UpdateView, CreateView,DeleteView, View
# Create your views here.
class Categorias(LoginRequiredMixin, View):
    model_categoria = Categoria
    model_plato = Plato
    template_name = 'menu/categoria/Categorias.html'

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