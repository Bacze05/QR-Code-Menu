"""
URL configuration for QRMenu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import logout_then_login,redirect_to_login
import menu.views as menuV
import panelAdmin as panelA
import users.views as users1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', menuV.ConfigMenu.as_view(),name='menuP'),
    path('menu/', include('menu.urls')),
    path('panelAdmin/', include('panelAdmin.urls')),
    path('user/', include('users.urls')),
    path('logout/', users1.exit, name='exit'),
    path('cambiar_password/', users1.CambiarPassword.as_view(), name='cambiar_password')


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)