"""g4car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home, cadastro_cliente, listagem_clientes, \
    cadastro_veiculo, listagem_veiculos, Registrar, atualiza_cliente, atualiza_veiculo, \
    exclui_cliente, exclui_veiculo, cadastro_parametro, listagem_parametros,\
    cadastro_mensalista, listagem_mensalistas, atualiza_parametro, exclui_parametro,\
    atualiza_mensalista, exclui_mensalista, cadastro_movimento, listagem_movimentos,\
    atualiza_movimento, exclui_movimento
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='url_principal'),
    path('registrar/', Registrar.as_view(), name='url_registrar'),
    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('listagem_clientes/', listagem_clientes, name='url_listagem_clientes'),
    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('listagem_veiculos/', listagem_veiculos, name='url_listagem_veiculos'),
    path('atualiza_cliente/<int:id>/', atualiza_cliente, name='url_atualiza_cliente'),
    path('atualiza_veiculo/<int:id>/', atualiza_veiculo, name='url_atualiza_veiculo'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculo'),
    path('cadastro_parametro/', cadastro_parametro, name='url_cadastro_parametro'),
    path('listagem_parametros/', listagem_parametros, name='url_listagem_parametros'),
    path('cadastro_mensalista/', cadastro_mensalista, name='url_cadastro_mensalista'),
    path('listagem_mensalistas/', listagem_mensalistas, name='url_listagem_mensalistas'),
    path('atualiza_parametro/<int:id>/', atualiza_parametro, name='url_atualiza_parametro'),
    path('exclui_parametro/<int:id>/', exclui_parametro, name='url_exclui_parametro'),
    path('atualiza_mensalista/<int:id>/', atualiza_mensalista, name='url_atualiza_mensalista'),
    path('exclui_mensalista/<int:id>/', exclui_mensalista, name='url_exclui_mensalista'),
    path('cadastro_movimento/', cadastro_movimento, name='url_cadastro_movimento'),
    path('listagem_movimentos/', listagem_movimentos, name='url_listagem_movimentos'),
    path('atualiza_movimento/<int:id>/', atualiza_movimento, name='url_atualiza_movimento'),
    path('exclui_movimento/<int:id>/', exclui_movimento, name='url_exclui_movimento'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
