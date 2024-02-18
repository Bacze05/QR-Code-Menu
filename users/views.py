from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.views.generic import TemplateView,ListView,UpdateView, CreateView,DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import *
from .forms import *
from .mixins import *


# USUARIOS CRUD

class Usuarios(SuperUsuariosMixin,LoginRequiredMixin,View):
    model=User
    form_class= CustomUserCreationForm
    template_name='user/UserList.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=1)
    def get_context_data(self, **kwargs):
        context = {}
        context["usuarios"] = self.get_queryset()
        context["form"] = self.form_class 
        return context
    
    def get(self,request,*args, **kwargs):  
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = serialize('json', self.get_queryset())
            return HttpResponse(data, 'application/json')
        else:
            return render(request,self.template_name,self.get_context_data())   
    
    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            # Si el formulario no es válido, renderiza la página nuevamente con el formulario y los errores
            context = self.get_context_data()
            context['form'] = form  # Agrega el formulario con errores al contexto
            return render(request, self.template_name, context)
        

class UsuarioEdicion(SuperUsuariosMixin,LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user/mantenedorUsuario.html'
    form_class = CustomUserEditForm
    success_url = reverse_lazy('usuarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            messages.success(self.request, "Modificado Correctamente")
            return redirect('usuarios')
        else:
            print("Formulario no válido:", form.errors.as_data())
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)
        
class UsuariosDeletes(SuperUsuariosMixin,LoginRequiredMixin,View):
    model=User
    form_class= CustomUserDeletionForm
    template_name='user/UserDeleteList.html'
    def get_queryset(self):
        return self.model.objects.filter(is_active=0)
    def get_context_data(self, **kwargs):
        context = {}
        context["usuarios"] = self.get_queryset()
        context["form"] = self.form_class 
        return context
    
    def get(self,request,*args, **kwargs):  
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = serialize('json', self.get_queryset())
            return HttpResponse(data, 'application/json')
        else:
            return render(request,self.template_name,self.get_context_data())   
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Procesar el formulario solo si es válido
            usuario_id = form.cleaned_data.get('usuario_id')
            usuario = get_object_or_404(User, id=usuario_id)
            usuario.delete()
            return redirect('usuariosDelete')
        else:
            # Si el formulario no es válido, renderiza la página nuevamente con el formulario y los errores
            context = self.get_context_data()
            context['form'] = form  # Agrega el formulario con errores al contexto
            return render(request, self.template_name, context)

# FUNCIONES PARA USUARIO
def obtener_nombre_grupo(request, group_id):
    try:
        grupo = Group.objects.get(pk=group_id)
        nombre_grupo = grupo.name
        return JsonResponse({'nombre_grupo': nombre_grupo})
    except Group.DoesNotExist:
        return JsonResponse({'nombre_grupo': 'Grupo no encontrado'}, status=404)

def desactivar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.is_active = False
    usuario.save()

    return redirect('usuariosDelete')

def activar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.is_active = True
    usuario.save()

    return redirect('usuariosDelete')

def exit(request):
    logout(request)
    return redirect('menuP')

class CambiarPassword(View):
    template_name="user/cambiar_password.html"
    form_class=CambiarPasswordForm
    success_url= reverse_lazy("panelAdmin")

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'form':self.form_class})
    
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         user = User.objects.filter(id=request.user.id)
    #         if user.exists():
    #             user = user.first()
    #             user.set_password(form.cleaned_data.get('password1'))
    #             return redirect(self.success_url)
    #         return redirect(self.success_url)
    #     else:
    #         form = self.form_class(request.POST)
    #         return render(request,self.template_name,{'form':form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user  # No necesitas filtrar por ID, ya tienes el usuario actual
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})
            
