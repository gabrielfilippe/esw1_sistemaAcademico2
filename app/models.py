from django.db import models

# Create your models here.

class Ocupacao(models.Model):
    class Meta:
        verbose_name = 'Ocupacao'
        verbose_name_plural = 'Ocupacoes'
    
    nome = models.CharField(max_length=100)
    
    
    
class Cidade(models.Model): 
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
    
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    
    

class Pessoa(models.Model):
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    
    nome = models.CharField(max_length=100)
    nome_do_pai = models.CharField(max_length=100)
    nome_da_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    data_nascimento = models.DateField(verbose_name = 'Data de nascimento')
    email = models.EmailField()
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    

class Instituicao_de_ensino(models.Model):   
    class Meta:
        verbose_name = 'Instituicao'
        verbose_name_plural = 'Instituicoes'
    
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    
    
class Area_do_saber(models.Model):
    class Meta:
        verbose_name = 'Area do saber'
        verbose_name_plural = 'Areas do saber'
    
    nome = models.CharField(max_length=100)
    


class Gerenciar_cursos(models.Model):
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField(default=0)
    duracao_meses = models.IntegerField(default=0)
    instituicao_de_ensino = models.ForeignKey(Instituicao_de_ensino, on_delete=models.CASCADE)

    
    

    