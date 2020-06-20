# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'cadastro'
urlpatterns = [
    # Dispositivo
    # /cadastro/dispositivo/adicionar/
    url(r'dispositivo/adicionar/$',
        views.AdicionarDispositivoView.as_view(), name='adddispositivoview'),
    # /cadastro/dispositivo/listadispositivos
    url(r'dispositivo/listadispositivos/$',
        views.DispositivosListView.as_view(), name='listadispositivosview'),
    # /cadastro/dispositivo/editar/
    url(r'dispositivo/editar/(?P<pk>[0-9]+)/$',
        views.EditarDispositivoView.as_view(), name='editardispositivoview'),

    # Peças
    # /cadastro/peça/adicionar/
    url(r'peça/adicionar/$',
        views.AdicionarPeçaView.as_view(), name='addpeçaview'),
    # /cadastro/peça/listapeças
    url(r'peça/listapeças/$',
        views.PeçasListView.as_view(), name='listapeçasview'),
    # /cadastro/peça/editar/
    url(r'peça/editar/(?P<pk>[0-9]+)/$',
        views.EditarPeçaView.as_view(), name='editarpeçaview'),

    # Tarefas
    # /cadastro/tarefa/adicionar/
    url(r'tarefa/adicionar/$',
        views.AdicionarTarefaView.as_view(), name='addtarefaview'),
    # /cadastro/tarefa/listapeças
    url(r'tarefa/listatarefas/$',
        views.TarefasListView.as_view(), name='listatarefasview'),
    # /cadastro/tarefa/editar/
    url(r'tarefa/editar/(?P<pk>[0-9]+)/$',
        views.EditarTarefaView.as_view(), name='editartarefaview'),

    # Troca de Peças
    # /cadastro/trocaPecas/adicionar/
    url(r'trocaPeca/adicionar/$',
        views.AdicionarTrocaPecaView.as_view(), name='addtrocaPecaview'),
    # /cadastro/trocaPeca/listatrocaPecas
    url(r'trocaPeca/listatrocaPecas/$',
        views.TrocaPecasListView.as_view(), name='listatrocaPecasview'),
    # /cadastro/trocaPeca/editar/
    url(r'trocaPeca/editar/(?P<pk>[0-9]+)/$',
        views.EditarTrocaPecaView.as_view(), name='editartrocaPecaview'),

    # Outros

    # Categorias
    # /cadastro/outros/adicionarcategoria/
    url(r'outros/adicionarcategoria/$',
        views.AdicionarCategoriaView.as_view(), name='addcategoriaview'),
    # /cadastro/outros/listacategorias/
    url(r'outros/listacategorias/$',
        views.CategoriasListView.as_view(), name='listacategoriasview'),
    # /cadastro/outros/editarcategoria/
    url(r'outros/editarcategoria/(?P<pk>[0-9]+)/$',
        views.EditarCategoriaView.as_view(), name='editarcategoriaview'),

    # Serviços
    # /cadastro/outros/adicionarservico/
    url(r'outros/adicionarservico/$',
        views.AdicionarServicoView.as_view(), name='addservicoview'),
    # /cadastro/outros/listaservicos/
    url(r'outros/listaservicos/$',
        views.ServicosListView.as_view(), name='listaservicosview'),
    # /cadastro/outros/editarservico/
    url(r'outros/editarservico/(?P<pk>[0-9]+)/$',
        views.EditarServicoView.as_view(), name='editarservicoview'),

    # Unidades
    # /cadastro/outros/adicionarunidade/
    url(r'outros/adicionarunidade/$',
        views.AdicionarUnidadeView.as_view(), name='addunidadeview'),
    # /cadastro/outros/listaunidades/
    url(r'outros/listaunidades/$',
        views.UnidadesListView.as_view(), name='listaunidadesview'),
    # /cadastro/outros/editarcunidade/
    url(r'outros/editarunidade/(?P<pk>[0-9]+)/$',
        views.EditarUnidadeView.as_view(), name='editarunidadeview'),

    # Marcas
    # /cadastro/outros/adicionarmarca/
    url(r'outros/adicionarmarca/$',
        views.AdicionarMarcaView.as_view(), name='addmarcaview'),
    # /cadastro/outros/listamarcas/
    url(r'outros/listamarcas/$',
        views.MarcasListView.as_view(), name='listamarcasview'),
    # /cadastro/outros/editarmarca/
    url(r'outros/editarmarca/(?P<pk>[0-9]+)/$',
        views.EditarMarcaView.as_view(), name='editarmarcaview'),

    # Departamentos
    # /cadastro/outros/adicionardepartamento/
    url(r'outros/adicionardepartamento/$',
        views.AdicionarDepartamentoView.as_view(), name='adddepartamentoview'),
    # /cadastro/outros/listadepartamentos/
    url(r'outros/listadepartamentos/$',
        views.DepartamentosListView.as_view(), name='listadepartamentosview'),
    # /cadastro/outros/editardepartamento/
    url(r'outros/editardepartamento/(?P<pk>[0-9]+)/$',
        views.EditarDepartamentoView.as_view(), name='editardepartamentoview'),

    # Colaboradores
    # /cadastro/outros/adicionarmarca/
    url(r'outros/adicionarcolaborador/$',
        views.AdicionarColaboradorView.as_view(), name='addcolaboradorview'),
    # /cadastro/outros/listacolaboradores/
    url(r'outros/listacolaboradores/$',
        views.ColaboradoresListView.as_view(), name='listacolaboradoresview'),
    # /cadastro/outros/editarcolaborador/
    url(r'outros/editarcolaborador/(?P<pk>[0-9]+)/$',
        views.EditarColaboradorView.as_view(), name='editarcolaboradorview'),

]
