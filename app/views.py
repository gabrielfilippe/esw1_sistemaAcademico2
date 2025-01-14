from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    context = {
    }
    return render(request, 'home.html', context)

def alunos(request):
    context = {
        'alunos': Aluno.objects.all()
    }
    
    return render(request, 'alunos.html', context)


def instituicoes(request):
    context = {
        'instituicoes': Instituicao.objects.all()
    }
    
    return render(request, 'instituicoes.html', context)

def cidades(request):
    context = {
        'cidades': Cidade.objects.all()
    }
    
    return render(request, 'cidades.html', context)


def ufs(request):
    context = {
        'ufs': Uf.objects.all()
    }
    
    return render(request, 'ufs.html', context)

def cursos(request):   
    context = {
        'cursos': Curso.objects.all()
    }
    
    return render(request, 'cursos.html', context)



