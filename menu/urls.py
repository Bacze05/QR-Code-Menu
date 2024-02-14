# urls.py
from django.urls import path
from .views import generar_qr

urlpatterns = [
    path('generar-qr/', generar_qr, name='generar_qr'),

]
