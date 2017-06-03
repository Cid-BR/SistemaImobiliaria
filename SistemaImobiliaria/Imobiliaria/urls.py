#Imobiliaria
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from SistemaImobiliaria.Imobiliaria import views as views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^novo_apartamento', views.novo_apartamento, name='novo_apartamento'),
    url(r'^nova_casa', views.nova_casa, name='nova_casa'),
    url(r'^nova_pessoa_fisica', views.nova_pessoa_fisica, name='pf'),
    url(r'^nova_pessoa_juridica', views.nova_pessoa_juridica, name='pj'),
    url(r'^nova_sala_comercial', views.nova_sala_comercial,
        name='nova_sala_comercial'),
    url(r'^novo_estabelecimento_comercial', views.novo_estabelecimento_comercial
    , name='novo_estabelecimento_comercial'),
    url(r'^novo_terreno_lote', views.novo_terreno_lote
    , name='novo_terreno_lote'),
    url(r'^nova_propriedade_rural', views.nova_propriedade_rural
    , name='nova_propriedade_rural'),
    url(r'^novo_empreendimento', views.novo_empreendimento
    , name='novo_empreendimento'),
    url(r'^novo_atendimento', views.novo_atendimento
    , name='novo_atendimento'),
    url(r'^nova_capitacao', views.nova_capitacao
    , name='nova_capitacao'),

    url(r'^exibir_pf', views.exibir_pf
    , name='exibir_pf'),
    url(r'^pesquisa_pf=(?P<valor>[\w-]+)', views.pesquisa_pf),
    url(r'^detalhes_pf=(?P<id>[\w-]+)', views.detalhes_pf),

    url(r'^exibir_pj', views.exibir_pj
    , name='exibir_pj'),
    url(r'^pesquisa_pj=(?P<valor>[\w-]+)', views.pesquisa_pj),
    url(r'^detalhes_pj=(?P<id>[\w-]+)', views.detalhes_pj),

    url(r'^exibir_apartamento', views.exibir_apartamento
    , name='exibir_apartamento'),
    url(r'^pesquisa_apartamento=(?P<valor>[\w-]+)', views.pesquisa_apartamento),
    url(r'^detalhes_apartamento=(?P<id>[\w-]+)', views.detalhes_apartamento),

    url(r'^exibir_casa', views.exibir_casa
    , name='exibir_casa'),
    url(r'^pesquisa_casa=(?P<valor>[\w-]+)', views.pesquisa_casa),
    url(r'^detalhes_casa=(?P<id>[\w-]+)', views.detalhes_casa),

    url(r'^exibir_salacomercial', views.exibir_salacomercial
    , name='exibir_salacomercial'),
    url(r'^pesquisa_salacomercial=(?P<valor>[\w-]+)',
        views.pesquisa_salacomercial),
    url(r'^detalhes_salacomercial=(?P<id>[\w-]+)',
        views.detalhes_salacomercial),

    url(r'^exibir_estabalecimentocomercial', views.exibir_estabalecimentocomercial
    , name='exibir_estabalecimentocomercial'),
    url(r'^pesquisa_estabalecimentocomercial=(?P<valor>[\w-]+)',
        views.pesquisa_estabalecimentocomercial),
    url(r'^detalhes_estabelecimentocomercial=(?P<id>[\w-]+)',
        views.detalhes_estabelecimentocomercial),

    url(r'^exibir_terrenolote', views.exibir_terrenolote
    , name='exibir_terrenolote'),
    url(r'^pesquisa_terrenolote=(?P<valor>[\w-]+)',
        views.pesquisa_terrenolote),
    url(r'^detalhes_terrenolote=(?P<id>[\w-]+)',
        views.detalhes_terrenolote),

    url(r'^exibir_propriedaderural', views.exibir_propriedaderural
    , name='exibir_propriedaderural'),
    url(r'^pesquisa_propriedaderural=(?P<valor>[\w-]+)',
        views.pesquisa_propriedaderural),
    url(r'^detalhes_propriedaderural=(?P<id>[\w-]+)',
        views.detalhes_propriedaderural),

    url(r'^exibir_empreendimento', views.exibir_empreendimento
    , name='exibir_empreendimento'),
    url(r'^pesquisa_empreendimento=(?P<valor>[\w-]+)',
        views.pesquisa_empreendimento),
    url(r'^detalhes_empreendimento=(?P<id>[\w-]+)',
        views.detalhes_empreendimento),

    url(r'^exibir_atendimento', views.exibir_atendimento
    , name='exibir_atendimento'),
    url(r'^pesquisa_atendimento',
        views.pesquisa_atendimento),
    url(r'^detalhes_atendimento=(?P<id>[\w-]+)',
        views.detalhes_atendimento),

    url(r'^realizar_pesquisa', views.realizar_pesquisa, 
        name='realizar_pesquisa'),

    url(r'^agendar=(?P<id_atendimento>[0-9]+)', views.agendar_visita, 
        name='agendar_visita'),    

    url(r'^exibir_captacao', views.exibir_captacao
    , name='exibir_capitacao'),
    url(r'^pesquisa_capitacao=(?P<valor>[\w-]+)',
        views.pesquisa_atendimento),
    url(r'^detalhes_capitacao=(?P<id>[\w-]+)',
        views.detalhes_capitacao),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
