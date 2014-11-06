# coding: utf-8
from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelform_factory
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


from contatos.core.forms import EmpresaForm
from contatos.core.models import CategoriaEmpresa, Empresa

CategoriaEmpresaForm = modelform_factory(CategoriaEmpresa)

index = TemplateView.as_view(template_name='index.html')

categoria_create = CreateView.as_view(
    model=CategoriaEmpresa,
    success_url=reverse_lazy('categoria_list'),
    form_class=CategoriaEmpresaForm
)
categoria_delete = DeleteView.as_view(
    template_name='confirm_delete.html',
    model=CategoriaEmpresa,
    success_url=reverse_lazy('categoria_list')
)
categoria_list = ListView.as_view(
    model=CategoriaEmpresa,
    paginate_by=15
)
categoria_update = UpdateView.as_view(
    model=CategoriaEmpresa,
    success_url=reverse_lazy('categoria_list')
)


empresa_create = CreateView.as_view(model=Empresa, success_url=reverse_lazy('empresa_list'), form_class=EmpresaForm)
empresa_delete = DeleteView.as_view(template_name='confirm_delete.html', model=Empresa, success_url=reverse_lazy('empresa_list'))
empresa_list = ListView.as_view(model=Empresa, paginate_by=15)
empresa_update = UpdateView.as_view(model=Empresa, success_url=reverse_lazy('empresa_list'), form_class=EmpresaForm)
