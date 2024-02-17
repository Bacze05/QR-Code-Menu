 #LOGIN
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    
    path('usuarios/desactivar/<int:pk>/', desactivar_usuario, name='desactivar_usuario'),
    path('usuarios/activar/<int:pk>/', activar_usuario, name='activar_usuario'),

    path('usuarios/',Usuarios.as_view(), name="usuarios"),
    path('usuariosDelete/',UsuariosDeletes.as_view(), name="usuariosDelete"),
    path('usuarios/edit/<int:pk>',UsuarioEdicion.as_view(),name='editarUsuario'),
    path('obtener_nombre_grupo/<int:group_id>/', obtener_nombre_grupo, name='obtener_nombre_grupo'),
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)