'''Here is the models'''
from markdownx.models import MarkdownxField
from django.db import models

class Instituicao(models.Model):
    '''Table of Institutions'''
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=10)
    estado = models.CharField(max_length=70)

class PET(models.Model):
    '''Table of PETs'''
    nome = models.CharField(max_length=200)
    instituicao = models.ForeignKey(Instituicao)

class Petiano(models.Model):
    '''Table of petianos'''
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    pet = models.ForeignKey(PET)

class Documento(models.Model):
    '''Table of files'''
    arquivo = models.FileField(upload_to='uploads/%Y/%m/%d/')

tipos_atividades = (('GDT', 'GDT'), ('Plenária', "Plenária"))

class Atividade(models.Model):
    '''Table of Activities'''
    tipo = models.CharField(max_length=20, choices=tipos_atividades)

class GDT(Atividade):
    '''Table of GDTs'''
    titulo = models.CharField(max_length=200)
    foi_divulgado = models.BooleanField()
    ordem = models.IntegerField()
    presidente = models.ForeignKey(Petiano)
    documentos = models.ManyToManyField(Documento)

class Encaminhamento(models.Model):
    '''Table of Encaminhamentos'''
    origem = models.ForeignKey(Atividade)
    corpo = MarkdownxField()
    situacao = models.BooleanField()

class Inscricao(models.Model):
    '''Table of Inscricoes'''
    petiano = models.OneToOneField(Petiano)
    gdt = models.ForeignKey(GDT)

class Pauta(models.Model):
    '''Table of Pautas'''
    titulo = models.CharField(max_length=200)
    encaminhamentos = models.ManyToManyField(Encaminhamento)

class Postagem(models.Model):
    '''Table of Posts'''
    titulo = models.CharField(max_length=200)
    corpo = MarkdownxField()
    data = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Petiano)

class ComponenteDaMesa(models.Model):
    '''Table of '''
    petiano = models.ForeignKey(Petiano)
    funcao = models.CharField(max_length=200)

class Assembleia(models.Model):
    '''Table of Assembleia'''
    regimento = models.ForeignKey(Documento)
    mesa = models.ManyToManyField(ComponenteDaMesa)
    pautas = models.ManyToManyField(Pauta)
    encaminhamento_atual = models.ForeignKey(Encaminhamento)
