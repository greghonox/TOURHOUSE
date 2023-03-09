from django.contrib import admin
from .models import Funcionario, Sede, Departamento


class FuncionarioAdmin(admin.ModelAdmin):
    list_filter = ['nome_completo', 'email', 'departamento_sede', 'ativo'] 
    list_display = list_filter

class SedeAdmin(admin.ModelAdmin):
    list_filter = ['cnpj',  'logradouro', 'cidade', 'pais']
    list_display = list_filter

class DepartamentoAdmin(admin.ModelAdmin):
    list_filter = ['centro_custo', 'codigo_integracao']
    list_display = list_filter

    

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Sede, SedeAdmin)
admin.site.register(Departamento, DepartamentoAdmin)