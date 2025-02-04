from django.urls import path
from .views import *

#Depois de criar as rotas, é necessário criar as views para cada uma delas.
#Primeiro parametro = O que vai aparecer na URL, segundo parametro = função que vai ser chamada, terceiro parametro = nome da rota

urlpatterns = [
    path('', home, name='home'),
    path('alunos/', alunos, name='alunos'),
    path('instituicoes/', instituicoes, name='instituicoes'),
    path('cidades/', cidades, name='cidades'), 
    path('ufs/', ufs, name='ufs'),
    path('cursos/', cursos, name='cursos'),
]
