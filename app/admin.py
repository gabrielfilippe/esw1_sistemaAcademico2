from django.contrib import admin
from .models import *

# Register your models here.

class PessoaInline(admin.StackedInline):
    model = Pessoa
    extra = 1

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [PessoaInline]


class CursoInline(admin.StackedInline):
    model = Curso
    extra = 1

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'site', 'telefone', 'cidade']  #são os campos que aparecem na tabela no admin
    inlines = [CursoInline]


@admin.register(AreaDoSaber)
class AreaDoSaberAdmin(admin.ModelAdmin):
    list_display = ['nome']
    

class DisciplinaInline(admin.StackedInline):
    model = Disciplina
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituicao', 'area_do_saber', 'carga_horaria_total', 'duracao_meses']
    inlines = [DisciplinaInline]

class AvaliacaoInline(admin.StackedInline):
    model = Avaliacao
    extra = 1

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'area_do_saber', 'curso']
    inlines = [AvaliacaoInline]


class CidadeInline(admin.StackedInline):
    model = Cidade
    extra = 1

@admin.register(Uf)
class UfAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [CidadeInline]

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    class FrequenciaInline(admin.StackedInline):
        model = Frequencia
        extra = 1
    
    class AvaliacaoInline(admin.StackedInline):
        model = Avaliacao
        extra = 1
    
    class DisciplinaInline(admin.StackedInline):
        model = Disciplina
        extra = 1
    
    inlines = [FrequenciaInline, DisciplinaInline, AvaliacaoInline]
        

admin.site.register(Cidade)








    




    







    
    