import io
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria, Plato

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
    

    # ------
# views.py
from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import io

# def generar_qr(request):
#     if request.method == 'POST':
#         qr_content = request.POST.get('qr_content', '')
#         if qr_content:
#             # Crear el objeto QRCode
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=10,
#                 border=4,
#             )
#             # Agregar el contenido al código QR
#             qr.add_data(qr_content)
#             qr.make(fit=True)
#             # Crear una imagen del código QR
#             img = qr.make_image(fill_color="black", back_color="white")
#             # Guardar la imagen en un buffer
#             buffer = io.BytesIO()
#             img.save(buffer, format='PNG')
#             qr_img_data = buffer.getvalue()
#             # Devolver la imagen del código QR en la respuesta HTTP
#             return HttpResponse(qr_img_data, content_type="image/png")
#     return render(request, 'panelAdmin/generar-qr.html', {'qr_image': None})

def generar_qr(request):
    if request.method == 'POST':
        qr_content = request.POST.get('qr_content', '')
        if qr_content:
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
    return render(request, 'panelAdmin/generar-qr.html', {'qr_image': None})








