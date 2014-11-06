# coding: utf-8

from django import forms

from contatos.core.models import CategoriaEmpresa, Empresa


class EmpresaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=CategoriaEmpresa.objects.all().order_by('-categoria'),
    )

    class Meta:
        model = Empresa
