from django.db import models


tipos_integracoes = (
    (0, 'erp'),
    (1, 'crm'),
    (2, 'bi'),
    (3, 'api'),
    (4, 'e-commerce'),
    (5, 'loT')
)
class Sede(models.Model):
    cnpj = models.CharField(verbose_name='Cnpj', max_length=14)
    logradouro = models.CharField(verbose_name='Logradouro', max_length=255)
    cidade = models.CharField(verbose_name='Cidade', max_length=255)
    pais = models.CharField(verbose_name='Pais', max_length=255)
    
    
class Departamento(models.Model):
    centro_custo = models.IntegerField(verbose_name='centro de custo')
    codigo_integracao = models.CharField(verbose_name='Integrações', choices=tipos_integracoes, max_length=1)
    
    
class Funcionario(models.Model):
    nome_completo = models.CharField(verbose_name='nome completo', max_length=255)
    email = models.CharField(verbose_name='email', max_length=255)
    telefone = models.CharField(verbose_name='telefone', max_length=255)
    data_nascimento = models.DateField(verbose_name='Data de nascimento', max_length=255)
    data_ingresso = models.DateField(verbose_name='Data de ingresso', max_length=255)
    data_desligamento = models.DateField(verbose_name='Data de desligamento', max_length=255)
    ativo = models.BooleanField(verbose_name='Ativo', default=True, max_length=255)
    cidade = models.CharField(verbose_name='Cidade', max_length=255)
    departamento_sede = models.ForeignKey('Departamento', 
        verbose_name='departamento_sede', on_delete=models.CASCADE)
    

