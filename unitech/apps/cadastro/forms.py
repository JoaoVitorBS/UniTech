# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Dispositivo, Unidade, Marca, Categoria, Servico, Departamento, Colaborador, Tarefa, Peça, TrocaPecas


class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ('codigo', 'descricao', 'categoria', 'marca', 'unidade', 'departamento', 'status', 'inf_adicionais')
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'status_servico': forms.Select(attrs={'class': 'form-control'}),
            'inf_adicionais': forms.Textarea(attrs={'class': 'form-control'}),

        }
        labels = {
            'codigo': _('Código'),
            'descricao': _('Descrição'),
            'categoria': _('Categoria'),
            'marca': _('Marca'),
            'unidade': _('Unidade'),
            'departamento': _('Departamento'),
            'status': _('Status'),
            'inf_adicionais': _('Informações adicionais'),

        }


class PeçaForm(forms.ModelForm):
    class Meta:
        model = Peça
        fields = ('codigo', 'peça_desc', 'categoria', 'marca', 'unidade', 'quantidade', 'estado', 'inf_adicionais')
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'peça_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'inf_adicionais': forms.Textarea(attrs={'class': 'form-control'}),

        }
        labels = {
            'codigo': _('Código'),
            'peça_desc': _('Descrição'),
            'categoria': _('Categoria'),
            'marca': _('Marca'),
            'unidade': _('Unidade'),
            'quantidade': _('Quantidade'),
            'estado': _('Estado'),
            'inf_adicionais': _('Informações adicionais'),

        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('categoria_desc',)
        widgets = {
            'categoria_desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'categoria_desc': _('Categoria'),
        }


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('marca_desc',)
        widgets = {
            'marca_desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'marca_desc': _('Marca'),
        }


class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = ('sigla_unidade', 'unidade_desc',)
        widgets = {
            'unidade_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla_unidade': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'unidade_desc': _('Descrição'),
            'sigla_unidade': _('Sigla'),
        }


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ('servico_desc',)
        widgets = {
            'servico_desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'servico_desc': _('Descrição'),
        }


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ('nome', 'telefone', 'cargo')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': _('Nome'),
            'telefone': _('Telefone'),
            'cargo': _('Cargo/Função'),
        }


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('departamento_desc', 'nome_responsavel', 'telefone_responsavel', 'email_responsavel')
        widgets = {
            'departamento_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'email_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'departamento_desc': _('Descrição'),
            'nome_responsavel': _('Nome do Responsável'),
            'telefone_responsavel': _('Telefone'),
            'email_responsavel': _('Email'),
        }


class TrocaPecaForm(forms.ModelForm):
    class Meta:
        model = TrocaPecas
        fields = ('status_servico', 'dispositivo', 'peca', 'motivo_troca', 'colaborador', 'inf_adicionais')
        widgets = {
            'status_servico': forms.Select(attrs={'class': 'form-control'}),
            'dispositivo': forms.Select(attrs={'class': 'form-control'}),
            'peca': forms.Select(attrs={'class': 'form-control'}),
            'motivo_troca': forms.TextInput(attrs={'class': 'form-control'}),
            'colaborador': forms.Select(attrs={'class': 'form-control'}),
            'inf_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'status_servico': _('Status'),
            'dispositivo': _('Dispositivo'),
            'peca': _('Peça'),
            'motivo_troca': _('Motivo da Troca'),
            'colaborador': _('Colaborador'),
            'inf_adicionais': _('Informações adicionais'),
        }


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('status_servico', 'dispositivo', 'defeito', 'servico', 'colaborador', 'inf_adicionais')
        widgets = {
            'status_servico': forms.Select(attrs={'class': 'form-control'}),
            'dispositivo': forms.Select(attrs={'class': 'form-control'}),
            'defeito': forms.TextInput(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),
            'colaborador': forms.Select(attrs={'class': 'form-control'}),
            'inf_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'status_servico': _('Status'),
            'dispositivo': _('Dispositivo'),
            'defeito': _('Defeito'),
            'servico': _('Serviço'),
            'colaborador': _('Colaborador'),
            'inf_adicionais': _('Informações adicionais'),
        }
