# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('falar_com', models.CharField(max_length=125, verbose_name='Falar com')),
                ('logradouro', models.CharField(max_length=255, null=True, verbose_name='Logradouro', blank=True)),
                ('numero', models.CharField(max_length=25, null=True, verbose_name='n\xfamero', blank=True)),
                ('complemento', models.CharField(max_length=200, null=True, verbose_name='complemento', blank=True)),
                ('bairro', models.CharField(max_length=200, null=True, verbose_name='bairro', blank=True)),
                ('municipio', models.CharField(max_length=200, null=True, verbose_name='Munic\xedpio', blank=True)),
                ('cep', models.CharField(max_length=10, null=True, verbose_name='CEP', blank=True)),
                ('site', models.URLField(null=True, blank=True)),
                ('categoria', models.ForeignKey(blank=True, to='core.CategoriaEmpresa', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
