# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('generar-qr/', generar_qr2, name='generar_qr'),
    path('categorias/edit/<int:pk>',CategoriaEdicion.as_view(),name='editarCategoria'),
    path('categorias/eliminado/<int:pk>/',CategoriaEliminar.as_view(),name='eliminarCategoria'),
    path('platolist/', PlatoG.as_view(), name='platolist'),
    path('plato/edit/<int:pk>',PlatoEdicion.as_view(),name='editarPlato'),
    path('plato/eliminado/<int:pk>/',PlatoEliminar.as_view(),name='eliminarPlato'),
]
