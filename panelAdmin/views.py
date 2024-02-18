
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from menu.models import Categoria
from django.core.serializers import serialize
from menu.forms import *


# Create your views here.


class PanelAdmin(LoginRequiredMixin,View):
    model=Categoria
    form_class= CategoriaCrearForm
    template_name='panelAdmin/panelAdmin.html'
    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = {}
        context["categorias"] = self.get_queryset()
        context["form"] = self.form_class 
        return context
    
    
    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = serialize('json', self.get_queryset())
            return HttpResponse(data, 'application/json')
        else:
            return render(request,self.template_name,self.get_context_data())  

    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('panelAdmin')
        else:
            # Si el formulario no es válido, vuelve a renderizar la página con el formulario y los errores
            context = self.get_context_data()
            context['form'] = form  # Pasar el formulario con los errores al contexto
            return render(request, self.template_name, context)
