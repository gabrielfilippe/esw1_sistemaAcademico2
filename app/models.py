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
    area_do_saber = models.ForeignKey(Area_do_saber, on_delete=models.CASCADE)

class Gerenciar_turnos(models.Model):
    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

    nome = models.CharField(max_length=100)

class Gerenciar_disciplinas(models.Model):
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
    
    nome = models.CharField(max_length=100)
    area_do_saber = models.ForeignKey(Area_do_saber, on_delete=models.CASCADE)

class Gerenciar_matriculas(models.Model):
    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    gerenciar_curso = models.ForeignKey(Gerenciar_cursos, on_delete=models.CASCADE)
    instituicao_de_ensino = models.ForeignKey(Instituicao_de_ensino, on_delete=models.CASCADE)
    data_inicio = models.DateField(verbose_name='Data Inicio')
    data_previsao_termino = models.DateField(verbose_name='Data Previsao Termino')

class Tipo_avaliacao(models.Model):
    class Meta:
        verbose_name = 'Tipo de avaliacao'
        verbose_name_plural = 'Tipos de avaliacoes'
    
    nome = models.CharField(max_length=100)


class Gerenciar_avaliacao(models.Model):
    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'

    descricao = models.CharField(max_length=100)
    gerenciar_cursos = models.ForeignKey(Gerenciar_cursos, on_delete= models.CASCADE)
    disciplinas = models.ForeignKey(Gerenciar_disciplinas, on_delete= models.CASCADE)
    nota = models.CharField(max_length=100)
    tipo_avaliacao = models.ForeignKey(Tipo_avaliacao, on_delete=models.CASCADE)


class Gerenciar_frequencia(models.Model):
    class Meta:
        verbose_name = 'Frequencia'
        verbose_name_plural = 'Frequencias'
    

    curso = models.ForeignKey(Gerenciar_cursos, on_delete= models.CASCADE)
    disciplina = models.ForeignKey(Gerenciar_disciplinas, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_de_faltas = models.IntegerField(default=0)


class Gerenciar_turmas(models.Model):
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
    

    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Gerenciar_turnos, on_delete=models.CASCADE)












    
    

    