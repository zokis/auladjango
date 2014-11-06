from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'contatos.core.views.index', name="index"),

    # Empresa
    url(r'^list/empresa/$', 'contatos.core.views.empresa_list', name="empresa_list"),
    url(r'^create/empresa/$', 'contatos.core.views.empresa_create', name="empresa_form"),
    url(r'^update/empresa/(?P<pk>\d+)/$', 'contatos.core.views.empresa_update', name="empresa_form"),
    url(r'^delete/empresa/(?P<pk>\d+)/$', 'contatos.core.views.empresa_delete', name="empresa_delete"),

    # Categoria
    url(r'^list/categoria/$', 'contatos.core.views.categoria_list', name="categoria_list"),
    url(r'^create/categoria/$', 'contatos.core.views.categoria_create', name="categoria_form"),
    url(r'^update/categoria/(?P<pk>\d+)/$', 'contatos.core.views.categoria_update', name="categoria_form"),
    url(r'^delete/categoria/(?P<pk>\d+)/$', 'contatos.core.views.categoria_delete', name="categoria_delete"),
)
