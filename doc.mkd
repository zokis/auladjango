Instalação
========

Python 2.7
----------

Entre em https://www.python.org/downloads/ e faça o Download do python 2.7.8

Instale em `C:\Python27`

Padrão windows: Next.. Next.. Netx.. Ok.. Ok.. Finish..

Adicionar ao Path do Windows:

Pressione:
windows+Pause

Vá em:

* Configurações avançadas do Sistema
* Variáveis de Ambiente
* Encontre o Path em Variáveis do sistema
* Editar...

Coloque ao final a string:
```
";C:\Python27;C:\Python27\Scripts;"
```

Ok.. Ok.. Ok..

SetupTools
----------

Salve a URL https://bootstrap.pypa.io/ez_setup.py como "ez_setup.py"

Abra o CMD

vá na pasta onde se encontra o arquivo e execute:

```
python ez_setup.py
```

ZZzzZzzzZZzzz

Django 1.7
----------

Faça o Download do Django:

https://www.djangoproject.com/download/1.7.1/tarball/


Descompacte o Django em qualquer pasta

Abra o CMD entre na pasta descompactada do Django e execute:

```
python setup.py install
```
zzzzZZzzzz

Adicionar o django-admin.py ao path

Execute os mesmo passos para que foram feitos para executar o python ao path, mas adicione a string:

```
";C:\Python27\Lib\site-packeges\Django\bin"
```

para testar se funcionou tente executar no CMD:

```
django-admin
```


Testar se Funcionou
-------------------

Execute no CMD o python e tente importar o django

```
import django
```


Criar o Projeto
===============

Crie uma pasta em `C:\` com o nome `django_contatos`

Abra o CMD e entre na pasta `cd C:\django_contatos` e execute:
```
django-admin startproject contatos
```

Para testar se o projeto esta funcionando entre na pasta `contatos` entro da pasta `django_contatos` pelo CMD e execute:

```
python manage.py runserver
```

Criar a app Principal do Sistema
==========================

No CMD entre na pasta `C:\django_contatos\contatos\contatos` e execute:

```
django-admin startapp core
```

Abra o arquivo `settings.py` com qualquer editor de texto e adicione a string `'contatos.core'` ao `INSTALLED_APPS`


Definir os Modelos
================

Abra o aquivo `models.py` e crie os Modelos:

```
class CategoriaEmpresa(models.Model):
    categoria = models.CharField(max_length=100)

    def __unicode__(self):
        return self.categoria


class Empresa(models.Model):
    nome = models.CharField(verbose_name=u'Nome', max_length=100)
    telefone = models.CharField(verbose_name=u'Telefone', max_length=20)
    falar_com = models.CharField(u'Falar com', max_length=125)
    categoria = models.ForeignKey(CategoriaEmpresa, null=True, blank=True)

    logradouro = models.CharField(u'Logradouro', max_length=255, null=True, blank=True)
    numero = models.CharField(u'número', max_length=25, null=True, blank=True)
    complemento = models.CharField(u'complemento', max_length=200, null=True, blank=True)
    bairro = models.CharField(u'bairro', max_length=200, null=True, blank=True)
    municipio = models.CharField(u'Município', max_length=200, null=True, blank=True)
    cep = models.CharField(u'CEP', max_length=10, null=True, blank=True)

    site = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.nome
```

No CMD vá até a raiz do projeto (pasta onde está o arquivo `manage.py`) e execute:

```
python manage.py syncdb
```

Ele irá perguntar se deseja criar um usuário digite: `yes`


Verficar se criou um arquivo chamado db.sqlite3 - Banco de dados, o nome é o definido na seguinte configuração do settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Criando a Primeira View
=======================

Abra o arquivo `views.py` e crie as Views:

```
# coding: utf-8
from django.views.generic import TemplateView

index = TemplateView.as_view(template_name='index.html')
```

Criando as URLs
=============

Abra o arquivo `urls.py` e deixe-o igual a este:
```
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'contatos.core.views.index', name="index"),
)
```

Criando o Template Inicial
==========================

Na pasta `core` crie uma pasta chamada `templates` e dentro dela um arquivo chamado `index.html` com o conteúdo:
```
<html>
    <head>
        <title>Início</title>
    </head>
    <body>
        Olá Mundo!!!
    </body>
</html>
```

Com um editor de texto adicione no `settings.py`:
```
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
```

Criando as views para a Categoria de Empresa
=====================================

Adicione ao arquivo `views.py`
```
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelform_factory

from contatos.core.models import CategoriaEmpresa

CategoriaEmpresaForm = modelform_factory(CategoriaEmpresa)

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
```

Criando as URLS para a Categoria de Empresa
=====================================

Adicione ao arquivo `urls.py` as urls:
```
# Categoria
url(r'^list/categoria/$', 'contatos.core.views.categoria_list', name="categoria_list"),
url(r'^create/categoria/$', 'contatos.core.views.categoria_create', name="categoria_form"),
url(r'^update/categoria/(?P<pk>\d+)/$', 'contatos.core.views.categoria_update', name="categoria_form"),
url(r'^delete/categoria/(?P<pk>\d+)/$', 'contatos.core.views.categoria_delete', name="categoria_delete"),
```

Criando os Templates de Categoria de Empresa
======================================

Na pasta `templates` cria um arquivo chamado `confirm_delete.html`:
```
<html>
    <head>
        <title>Deletar</title>
    </head>
    <body>
        <form method="post">
            {% csrf_token %}
            <h4>Você tem certeza que deseja deletar "{{ object }}"?</h4>
            <input type="submit" value="Confirmar" class="btn btn-danger" />
        </form>
    </body>
</html>
```


Na pasta `templates` cria uma pasta chamada `core` dentro dela crie os arquivos:
`categoriaempresa_form.html`
```
<html>
    <head>
        <title>Formulário</title>
    </head>
    <body>
        <form method="POST">
            {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" >
                {% if not form.instance.pk %}
                    Cadastrar
                {% else %}
                    Alterar
                {% endif %}
                </button>
                <input type="reset" value="Cancelar" />
            </div>
        </form>
    </body>
</html>
```
`categoriaempresa_list.html`
```
<html>
    <head>
        <title>Listagem</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>categoria</th>
                    <th style="width: 60px;">deletar</th>
                </tr>
            </thead>
            <tbody>
                {% for categoriaempresa in object_list %}
                <tr>
                    <td><a href="{% url 'categoria_form' categoriaempresa.pk %}">{{ categoriaempresa.categoria }}</a></td>
                    <td>
                        <a href="{% url 'categoria_delete' categoriaempresa.pk %}" class="btn btn-small btn-danger">
                            X
                        </a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <div class="pagination">
            <span class="step-links">
                {% if page_obj.has_previous %}
                    <a href="?page={{ page_obj.previous_page_number }}">previous</a>
                {% endif %}

                <span class="current">
                    Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}.
                </span>

                {% if page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}">next</a>
                {% endif %}
            </span>
        </div>
    </body>
</html>
```

Repita os passos para o Modelo de Empresa
===================================

Editar o Formulário da Empresa
==========================

Na pasta `core` crie um arquivo chamado `forms.py` com o conteúdo:
```
# coding: utf-8

from django import forms

from contatos.core.models import CategoriaEmpresa, Empresa


class EmpresaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=CategoriaEmpresa.objects.all().order_by('-categoria'),
    )

    class Meta:
        model = Empresa

```

No arquivo `views.py` importe o formulário recém criado:
```
from contatos.core.forms import EmpresaForm
```

Substitua o `EmpresaForm` antigo pelo novo e apague o antigo 

Deixando as Coisas Bonitas
======================

Na pasta `templates` crie um arquivo chamado `base.html` com o conteúdo:
```
{% load staticfiles %}
<html>
    <head>
        <title>{% block title %}Início{% endblock %}</title>
    </head>
    <body>
        {% block content %}Olá Mundo!!!{% endblock %}
    </body>
</html>
```
Altere o conteúdo do arquivo `index.html` para:
```
{% extends "base.html" %}
```

Faça o mesmo para todos os outros templates.
Exemplo `confirm_delete.html`:
```
{% extends "base.html" %}

{% block title %}
    Deletar {{ object }}
{% endblock %}

{% block content %}
<form method="post">
    {% csrf_token %}
    <h4>Você tem certeza que deseja deletar "{{ object }}"?</h4>
    <input type="submit" value="Confirmar" class="btn btn-danger" />
</form>
{% endblock content %}
```

Dentro da Pasta `core` crie uma pasta chamda `static` com uma pasta dentro chamda `css`
Acesse http://bootswatch.com/flatly/bootstrap.min.css e salve o arquivo nessa pasta com o nome `bootstrap.min.css`

Altere o arquivo base.html` para:
```
{% load staticfiles %}
<html>
    <head>
        <title>{% block title %}Início{% endblock %}</title>
    </head>
    <link rel="stylesheet" type="text/css" media="screen" href="{% static 'css/bootstrap.min.css'%}">
    <body>
        <nav class="navbar navbar-default" role="navigation">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                        <span class="sr-only">Toggle navigation</span>
                    </button>
                    <a class="navbar-brand" href="{% url 'index' %}">Início</a>
                </div>
                <div class="collapse navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="{% url 'empresa_list' %}">Listagem de Empresas</a></li>
                        <li><a href="{% url 'categoria_list' %}">Listagem de Categorias de Empresas</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        {% block content %}Olá Mundo!!!{% endblock %}
    </body>
</html>
```

Para criar botões de novo abra os templates de Listagem e adicionem um link:
```
<a href="{% url 'empresa_form' %}" class="btn btn-primary">Nova Empresa</a>
```
Faça a mesma coisa para Categoria de Empresa

Nos templates de listagem adicione as classes `"table table-bordered table-striped"` para as tabelas, ficando assim:
```
...
<table class="table table-bordered table-striped">
    ...
</table>
...
```