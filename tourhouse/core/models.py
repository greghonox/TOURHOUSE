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
    
    def __str__(self):
        return f'{self.id} {self.cnpj} {self.cidade}'
    
    
class Departamento(models.Model):
    centro_custo = models.IntegerField(verbose_name='centro de custo')
    codigo_integracao = models.IntegerField(verbose_name='Integrações', choices=tipos_integracoes)

    def get_codigo_integracao_display(self):
        return dict(tipos_integracoes)[self.codigo_integracao]
        
    def __str__(self):
        return f'{self.centro_custo} {self.get_codigo_integracao_display()}'


    class Meta:
        unique_together = (('centro_custo', 'codigo_integracao'))
    
class Funcionario(models.Model):
    nome_completo = models.CharField(verbose_name='nome completo', max_length=255)
    email = models.CharField(verbose_name='email', max_length=255, unique=True)
    telefone = models.CharField(verbose_name='telefone', max_length=20)
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    data_ingresso = models.DateField(verbose_name='Data de ingresso', auto_created=True)
    data_desligamento = models.DateField(verbose_name='Data de desligamento', null=True, blank=True)
    ativo = models.BooleanField(verbose_name='Ativo', default=True, max_length=255)
    cidade = models.CharField(verbose_name='Cidade', max_length=255)
    departamento_sede = models.ForeignKey('Departamento', 
        verbose_name='departamento_sede', on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.id} {self.nome_completo} {self.email}'


