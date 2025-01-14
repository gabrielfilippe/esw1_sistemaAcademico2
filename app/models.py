from django.db import models

# Create your models here.

class Ocupacao(models.Model):
    class Meta:
        verbose_name = 'Ocupação'
        verbose_name_plural = 'Ocupações'
    
    nome = models.CharField(max_length=100, verbose_name='Nome da ocupação')

    def __str__(self):
        return f'{self.nome}' #definição de como vai aparecer após ser salvo algum objeto na área administrativa


class Uf(models.Model):
    class Meta:
        verbose_name = 'UF'
        verbose_name_plural = 'UFS'

    nome = models.CharField(max_length = 100)
    abreviacao_uf = models.CharField(max_length = 2)

    def __str__(self):
        return self.nome
    
    
class Cidade(models.Model): 
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
    
    nome = models.CharField(max_length=100, verbose_name='Cidade')
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE, verbose_name = 'UF')

#função para formatar a forma de saída no admin
    def __str__(self):
        return f'{self.nome} - {self.uf.nome}'


    
    

class Pessoa(models.Model):
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    
    nome = models.CharField(max_length=100, verbose_name= 'Nome')
    nome_do_pai = models.CharField(max_length=100, verbose_name='Nome do pai')
    nome_da_mae = models.CharField(max_length=100, verbose_name = 'Nome da mãe')
    cpf = models.CharField(max_length=100, verbose_name = 'CPF')
    data_nascimento = models.DateField(verbose_name = 'Data de nascimento')
    email = models.EmailField(verbose_name='Email')
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name='Nome da ocupação')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name='Cidade')
    

    def __str__(self):
        return f'{self.nome}'


class Professor(Pessoa):
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return f'{self.nome}'



class Instituicao(models.Model):   
    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'
    
    nome = models.CharField(max_length=100, verbose_name='Nome instituição')
    site = models.CharField(max_length=100, verbose_name='Site')
    telefone = models.CharField(max_length=100, verbose_name='Telefone')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name='Cidade')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')

    def __str__(self):
        return f'{self.nome}'
    
    
    
class AreaDoSaber(models.Model):
    class Meta:
        verbose_name = 'Área do saber'
        verbose_name_plural = 'Áreas do saber'
    
    nome = models.CharField(max_length=100, verbose_name='Nome da Área do saber')

    def __str__(self):
        return f'{self.nome}'
    


class Curso(models.Model):
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    nome = models.CharField(max_length=100, verbose_name='Nome do curso')
    carga_horaria_total = models.IntegerField(default=0, verbose_name='Carga horaria total')
    duracao_meses = models.IntegerField(default=0, verbose_name='Duração meses')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Nome instituição')
    area_do_saber = models.ForeignKey(AreaDoSaber, on_delete=models.CASCADE, verbose_name='Nome Área do saber')


    def __str__(self):
        return f'{self.nome} - {self.instituicao.nome}'


class Turno(models.Model):
    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

    nome = models.CharField(max_length=100, verbose_name='Nome do turno')

    def __str__(self):
        return f'{self.nome}'


class Aluno(Pessoa):
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')

    def __str__(self):
        return f'{self.nome}'



class Disciplina(models.Model):
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
    
    nome = models.CharField(max_length=100, verbose_name='Nome da Disciplina')
    area_do_saber = models.ForeignKey(AreaDoSaber, on_delete=models.CASCADE, verbose_name='Nome área do saber')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name = 'Aluno')

    def __str__(self):
        return f'{self.nome}'


class Matricula(models.Model):
    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Nome')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Nome Instituição')
    data_inicio = models.DateField(verbose_name='Data Início')
    data_previsao_termino = models.DateField(verbose_name='Data Previsao Término')

    def __str__(self):
        return f'{self.nome}'

class TipoAvaliacao(models.Model):
     class Meta:
         verbose_name = 'Tipo de avaliação'
         verbose_name_plural = 'Tipos de avaliações'
    
     nome = models.CharField(max_length=100, verbose_name='Nome')

     def __str__(self):
         return f'{self.nome}'


class Avaliacao(models.Model):
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    descricao = models.CharField(max_length=100, verbose_name='Descricao')
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete= models.CASCADE, verbose_name='Disciplina')
    nota = models.CharField(max_length=100, verbose_name='Nota')
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE, verbose_name='Tipo Avaliação')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name='Aluno')

    def __str__(self):
        return f'{self.nome}'


class Frequencia(models.Model):
    class Meta:
        verbose_name = 'Frequência'
        verbose_name_plural = 'Frequências'
    

    curso = models.ForeignKey(Curso, on_delete= models.CASCADE, verbose_name= 'Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    numero_de_faltas = models.IntegerField(default=0, verbose_name='Número de Faltas')

    def __str__(self):
        return f'{self.nome}'


class Turma(models.Model):
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
    

    nome = models.CharField(max_length=100, verbose_name='Nome')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name='Turno')

    def __str__(self):
        return f'{self.nome}'


class Ocorrencia(models.Model):
    class Meta:
        verbose_name = 'Ocorrencia'
        verbose_name_plural = 'Ocorrencias'
    
    descricao = models.CharField(max_length=100, verbose_name='Descricão')
    data = models.DateField(verbose_name='Data')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')

    def __str__(self):
        return f'{self.nome}'




    
    

    
    






















    
    

    