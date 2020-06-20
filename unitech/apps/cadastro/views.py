from django.urls import reverse_lazy

from unitech.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from unitech.apps.cadastro.forms import DispositivoForm, CategoriaForm, UnidadeForm, MarcaForm, ServicoForm, \
    DepartamentoForm, TarefaForm, ColaboradorForm, PeçaForm, TrocaPecaForm
from .models import Dispositivo, Categoria, Unidade, Marca, Departamento, Servico, Colaborador, Tarefa, Peça, TrocaPecas


# ---------- Dispositivo ----------
class AdicionarDispositivoView(CustomCreateView):
    form_class = DispositivoForm
    template_name = "cadastro/gerais/dispositivo_add.html"
    success_url = reverse_lazy('cadastro:listadispositivosview')
    success_message = "Dispositivo <b>%(descricao)s </b>adicionado com sucesso."
    permission_codename = 'add_dispositivo'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(AdicionarDispositivoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR DISPOSITIVO'
        context['return_url'] = reverse_lazy('cadastro:listadispositivosview')
        return context

    def get(self, request, *args, **kwargs):
        return super(AdicionarDispositivoView, self).get(request, *args, **kwargs)


class DispositivosListView(CustomListView):
    template_name = 'cadastro/gerais/dispositivo_list.html'
    model = Dispositivo
    context_object_name = 'all_dispositivos'
    success_url = reverse_lazy('cadastro:listadispositivosview')
    permission_codename = 'view_dispositivo'

    def get_context_data(self, **kwargs):
        context = super(DispositivosListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'DISPOSITIVOS CADASTRADOS'
        context['add_url'] = reverse_lazy('cadastro:adddispositivoview')
        return context


class EditarDispositivoView(CustomUpdateView):
    form_class = DispositivoForm
    model = Dispositivo
    template_name = "cadastro/gerais/dispositivo_edit.html"
    success_url = reverse_lazy('cadastro:listadispositivosview')
    success_message = "Dispositivo <b>%(descricao)s </b>editado com sucesso."
    permission_codename = 'change_dispositivo'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(EditarDispositivoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listadispositivosview')
        return context


# ---------- Peças ----------
class AdicionarPeçaView(CustomCreateView):
    form_class = PeçaForm
    template_name = "cadastro/gerais/peça_add.html"
    success_url = reverse_lazy('cadastro:listapeçasview')
    success_message = "Peça <b>%(descricao)s </b>adicionada com sucesso."
    permission_codename = 'add_peça'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(AdicionarPeçaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR PEÇA'
        context['return_url'] = reverse_lazy('cadastro:listapeçasview')
        return context

    def get(self, request, *args, **kwargs):
        return super(AdicionarPeçaView, self).get(request, *args, **kwargs)


class PeçasListView(CustomListView):
    template_name = 'cadastro/gerais/peça_list.html'
    model = Peça
    context_object_name = 'all_peças'
    success_url = reverse_lazy('cadastro:listapeçasview')
    permission_codename = 'view_peça'

    def get_context_data(self, **kwargs):
        context = super(PeçasListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'PEÇAS CADASTRADAS'
        context['add_url'] = reverse_lazy('cadastro:addpeçaview')
        return context


class EditarPeçaView(CustomUpdateView):
    form_class = PeçaForm
    model = Peça
    template_name = "cadastro/gerais/peça_edit.html"
    success_url = reverse_lazy('cadastro:listapeçasview')
    success_message = "Peça <b>%(descricao)s </b>editada com sucesso."
    permission_codename = 'change_peça'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(EditarPeçaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listapeçasview')
        return context


# ---------- Tarefas ----------
class AdicionarTarefaView(CustomCreateView):
    form_class = TarefaForm
    template_name = "cadastro/gerais/tarefa_add.html"
    success_url = reverse_lazy('cadastro:listatarefasview')
    success_message = "Tarefa <b>%(descricao)s </b>adicionada com sucesso."
    permission_codename = 'add_tarefa'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTarefaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR TAREFA'
        context['return_url'] = reverse_lazy('cadastro:listatarefasview')
        return context

    def get(self, request, *args, **kwargs):
        return super(AdicionarTarefaView, self).get(request, *args, **kwargs)


class TarefasListView(CustomListView):
    template_name = 'cadastro/gerais/tarefa_list.html'
    model = Tarefa
    context_object_name = 'all_tarefas'
    success_url = reverse_lazy('cadastro:listatarefasview')
    permission_codename = 'view_tarefa'

    def get_context_data(self, **kwargs):
        context = super(TarefasListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'TAREFAS CADASTRADAS'
        context['add_url'] = reverse_lazy('cadastro:addtarefaview')
        return context


class EditarTarefaView(CustomUpdateView):
    form_class = TarefaForm
    model = Tarefa
    template_name = "cadastro/gerais/trocaPeca_edit.html"
    success_url = reverse_lazy('cadastro:listatrocaTrocaPecasview')
    success_message = "Troca de Peça <b>%(descricao)s </b>editada com sucesso."
    permission_codename = 'change_trocaPeça'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(EditarTarefaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listatrocaPeçasview')
        return context


# ---------- Troca de peças ----------
class AdicionarTrocaPecaView(CustomCreateView):
    form_class = TrocaPecaForm
    template_name = "cadastro/gerais/trocaPeca_add.html"
    success_url = reverse_lazy('cadastro:listatrocaPecasview')
    success_message = "Troca de Peças <b>%(descricao)s </b>adicionada com sucesso."
    permission_codename = 'add_trocaPeca'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTrocaPecaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'TROCA DE PEÇAS'
        context['return_url'] = reverse_lazy('cadastro:listatrocaPecasview')
        return context

    def get(self, request, *args, **kwargs):
        return super(AdicionarTrocaPecaView, self).get(request, *args, **kwargs)


class TrocaPecasListView(CustomListView):
    template_name = 'cadastro/gerais/trocaPeca_list.html'
    model = TrocaPecas
    context_object_name = 'all_trocaPecas'
    success_url = reverse_lazy('cadastro:listatrocaPecasview')
    permission_codename = 'view_trocaPeca'

    def get_context_data(self, **kwargs):
        context = super(TrocaPecasListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'TROCAS DE PEÇA'
        context['add_url'] = reverse_lazy('cadastro:addtrocaPecaview')
        return context


class EditarTrocaPecaView(CustomUpdateView):
    form_class = TrocaPecaForm
    model = TrocaPecas
    template_name = "cadastro/gerais/trocaPeca_edit.html"
    success_url = reverse_lazy('cadastro:listatrocaPecasview')
    success_message = "Troca de Peças <b>%(descricao)s </b>editada com sucesso."
    permission_codename = 'change_trocaPeca'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(EditarTrocaPecaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listatrocaPecasview')
        return context


# ---------- Outros ----------
class AdicionarOutrosBaseView(CustomCreateView):
    template_name = "base/popup_form.html"

    def get_context_data(self, **kwargs):
        context = super(AdicionarOutrosBaseView,
                        self).get_context_data(**kwargs)
        context['titulo'] = 'Adicionar ' + self.model.__name__
        return context


class EditarOutrosBaseView(CustomUpdateView):
    template_name = "base/popup_form.html"

    def get_context_data(self, **kwargs):
        context = super(EditarOutrosBaseView,
                        self).get_context_data(**kwargs)
        context['titulo'] = 'Editar {0}: {1}'.format(
            self.model.__name__, str(self.object))
        return context


# ---------- Categoria ----------
class AdicionarCategoriaView(AdicionarOutrosBaseView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('cadastro:addcategoriaview')
    permission_codename = 'add_categoria'


class CategoriasListView(CustomListView):
    model = Categoria
    template_name = 'cadastro/gerais/categoria_list.html'
    context_object_name = 'all_categorias'
    success_url = reverse_lazy('cadastro:listacategoriasview')
    permission_codename = 'view_categoria'


class EditarCategoriaView(EditarOutrosBaseView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('cadastro:listacategoriasview')
    permission_codename = 'change_categoria'


# ---------- Unidade ----------
class AdicionarUnidadeView(AdicionarOutrosBaseView):
    form_class = UnidadeForm
    model = Unidade
    success_url = reverse_lazy('cadastro:addunidadeview')
    permission_codename = 'add_unidade'


class UnidadesListView(CustomListView):
    model = Unidade
    template_name = 'cadastro/gerais/unidade_list.html'
    context_object_name = 'all_unidades'
    success_url = reverse_lazy('cadastro:listaunidadesview')
    permission_codename = 'view_unidade'


class EditarUnidadeView(EditarOutrosBaseView):
    form_class = UnidadeForm
    model = Unidade
    success_url = reverse_lazy('cadastro:listaunidadesview')
    permission_codename = 'change_unidade'


# ---------- Marca ----------
class AdicionarMarcaView(AdicionarOutrosBaseView):
    form_class = MarcaForm
    model = Marca
    success_url = reverse_lazy('cadastro:addmarcaview')
    permission_codename = 'add_marca'


class MarcasListView(CustomListView):
    model = Marca
    template_name = 'cadastro/gerais/marca_list.html'
    context_object_name = 'all_marcas'
    success_url = reverse_lazy('cadastro:listamarcasview')
    permission_codename = 'view_marca'


class EditarMarcaView(EditarOutrosBaseView):
    form_class = MarcaForm
    model = Marca
    success_url = reverse_lazy('cadastro:listamarcasview')
    permission_codename = 'change_marca'


# ---------- Serviço ----------
class AdicionarServicoView(AdicionarOutrosBaseView):
    form_class = ServicoForm
    model = Servico
    success_url = reverse_lazy('cadastro:addservicoview')
    permission_codename = 'add_servico'


class ServicosListView(CustomListView):
    model = Servico
    template_name = 'cadastro/gerais/servico_list.html'
    context_object_name = 'all_servicos'
    success_url = reverse_lazy('cadastro:listaservicosview')
    permission_codename = 'view_servico'


class EditarServicoView(EditarOutrosBaseView):
    form_class = ServicoForm
    model = Servico
    success_url = reverse_lazy('cadastro:listaservicosview')
    permission_codename = 'change_servico'


# ---------- Departamento ----------
class AdicionarDepartamentoView(AdicionarOutrosBaseView):
    form_class = DepartamentoForm
    model = Departamento
    success_url = reverse_lazy('cadastro:adddepartamentoview')
    permission_codename = 'add_departamento'


class DepartamentosListView(CustomListView):
    model = Departamento
    template_name = 'cadastro/gerais/departamento_list.html'
    context_object_name = 'all_departamentos'
    success_url = reverse_lazy('cadastro:listadepartamentosview')
    permission_codename = 'view_departamento'


class EditarDepartamentoView(EditarOutrosBaseView):
    form_class = DepartamentoForm
    model = Departamento
    success_url = reverse_lazy('cadastro:listadepartamentosview')
    permission_codename = 'change_departamento'


# ---------- Colaborador ----------
class AdicionarColaboradorView(AdicionarOutrosBaseView):
    form_class = ColaboradorForm
    model = Colaborador
    success_url = reverse_lazy('cadastro:addcolaboradorview')
    permission_codename = 'add_colaborador'


class ColaboradoresListView(CustomListView):
    model = Marca
    template_name = 'cadastro/gerais/colaborador_list.html'
    context_object_name = 'all_colaboradores'
    success_url = reverse_lazy('cadastro:listacolaboradoresview')
    permission_codename = 'view_colaborador'


class EditarColaboradorView(EditarOutrosBaseView):
    form_class = ColaboradorForm
    model = Colaborador
    success_url = reverse_lazy('cadastro:listacolaboradoresview')
    permission_codename = 'change_colaborador'
