# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assembleia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('GDT', 'GDT'), ('Plenária', 'Plenária')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ComponenteDaMesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Encaminhamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpo', markdownx.models.MarkdownxField()),
                ('situacao', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sigla', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Pauta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('encaminhamentos', models.ManyToManyField(to='evento.Encaminhamento')),
            ],
        ),
        migrations.CreateModel(
            name='PET',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Instituicao')),
            ],
        ),
        migrations.CreateModel(
            name='Petiano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=200)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.PET')),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('corpo', markdownx.models.MarkdownxField()),
                ('data', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Petiano')),
            ],
        ),
        migrations.CreateModel(
            name='GDT',
            fields=[
                ('atividade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evento.Atividade')),
                ('titulo', models.CharField(max_length=200)),
                ('foi_divulgado', models.BooleanField()),
                ('ordem', models.IntegerField()),
                ('documentos', models.ManyToManyField(to='evento.Documento')),
                ('presidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Petiano')),
            ],
            bases=('evento.atividade',),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='petiano',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='evento.Petiano'),
        ),
        migrations.AddField(
            model_name='encaminhamento',
            name='origem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Atividade'),
        ),
        migrations.AddField(
            model_name='componentedamesa',
            name='petiano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Petiano'),
        ),
        migrations.AddField(
            model_name='assembleia',
            name='encaminhamento_atual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Encaminhamento'),
        ),
        migrations.AddField(
            model_name='assembleia',
            name='mesa',
            field=models.ManyToManyField(to='evento.ComponenteDaMesa'),
        ),
        migrations.AddField(
            model_name='assembleia',
            name='pautas',
            field=models.ManyToManyField(to='evento.Pauta'),
        ),
        migrations.AddField(
            model_name='assembleia',
            name='regimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Documento'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='gdt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.GDT'),
        ),
    ]