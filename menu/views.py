import io
import qrcode
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.serializers import serialize
from django.contrib import messages
from django.views.generic import TemplateView,ListView,UpdateView, CreateView,DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria, Plato
from .forms import *

class ConfigMenu( View):
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
    
#qrcode 2 con contenido definido desde la view 


def generar_qr2(LoginRequiredMixin,request):
    # Definir el contenido del código QR
    qr_content = "https://getbootstrap.com/docs/5.3/customize/css-variables/"

    # Crear el objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Agregar el contenido al código QR
    qr.add_data(qr_content)
    qr.make(fit=True)
    # Crear una imagen del código QR
    img = qr.make_image(fill_color="black", back_color="white")
    # Guardar la imagen en un buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    qr_img_data = buffer.getvalue()
    # Devolver la imagen del código QR en la respuesta HTTP
    response = HttpResponse(qr_img_data, content_type="image/png")
    # Establecer el encabezado de Content-Disposition para forzar la descarga del archivo
    response['Content-Disposition'] = 'attachment; filename="codigo_qr.png"'
    return response




class CategoriaEdicion(LoginRequiredMixin,UpdateView):
    model=Categoria
    form_class=CategoriaForm
    template_name='menu/mantenedorCategoria.html'
    success_url= reverse_lazy('panelAdmin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        return context
    
class CategoriaEliminar(LoginRequiredMixin,DeleteView):
    model=Categoria
    success_url = reverse_lazy('panelAdmin')

    def form_valid(self,form):
        messages.success(self.request, "Eliminado Correctamente")
        return super().form_valid(form)
    
class PlatoG(LoginRequiredMixin,View):
    model=Plato
    form_class= PlatoForm
    template_name='menu/platolist.html'
    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = {}
        context["platos"] = self.get_queryset()
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
            return redirect('platolist')
        else:
            # Si el formulario no es válido, vuelve a renderizar la página con el formulario y los errores
            context = self.get_context_data()
            context['form'] = form  # Pasar el formulario con los errores al contexto
            return render(request, self.template_name, context)

class PlatoEdicion(LoginRequiredMixin,UpdateView):
    model=Plato
    form_class=PlatoForm
    template_name='menu/mantenedorPlato.html'
    success_url= reverse_lazy('platolist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["platos"] = Plato.objects.all()
        return context
    
class PlatoEliminar(LoginRequiredMixin,DeleteView):
    model=Plato
    success_url = reverse_lazy('platolist')

    def form_valid(self,form):
        messages.success(self.request, "Eliminado Correctamente")
        return super().form_valid(form)






