# coding: utf-8

from django.db import models


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
