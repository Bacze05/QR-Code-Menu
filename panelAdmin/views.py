from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from menu.models import Categoria
from django.core.serializers import serialize


# Create your views here.


class PanelAdmin(View):
    model=Categoria
    template_name='panelAdmin/panelAdmin.html'
    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = {}
        context["categorias"] = self.get_queryset()
        return context
    
    
    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = serialize('json', self.get_queryset())
            return HttpResponse(data, 'application/json')
        else:
            return render(request,self.template_name,self.get_context_data())  
    
    # def get(self,request,*args, **kwargs):  
    #     return render(request,self.template_name,self.get_context_data())

    


# class Categorias(LoginRequiredMixin,View):
#     model=Category
#     form_class= CategoryForm
#     template_name='inventario/Categorias.html'
#     def get_queryset(self):
#         return self.model.objects.all()
    
#     def get_context_data(self, **kwargs):
#         context = {}
#         context["categorias"] = self.get_queryset()
#         context["form"] = self.form_class 
#         return context
    
#     def get(self,request,*args, **kwargs):  
#         return render(request,self.template_name,self.get_context_data())
    
#     def post(self,request,*args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('categorias')