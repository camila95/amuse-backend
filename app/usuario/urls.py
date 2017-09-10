from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^persona/$', PersonaListCreateView.as_view(), name='lista_persona'),
    url(r'^acudiente/$', AcudienteListCreateView.as_view(), name='crear_persona'),
    url(r'^telefono/$', TelefonoListCreateView.as_view(), name='telefono_persona'),
]
