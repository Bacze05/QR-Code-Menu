from django.urls import path
from .views import *

urlpatterns = [
    path('panel/', PanelAdmin.as_view(), name='panelAdmin'),
    

]