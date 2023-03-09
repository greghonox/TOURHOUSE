from rest_framework import serializers
from rest_framework.response import Response
from core.models import Funcionario, Sede, Departamento


class FuncionarioSerializer(serializers.ModelSerializer):
    """Class to Funcionario"""

    class Meta:
        model = Funcionario
        fields = "__all__"

class SedeSerializer(serializers.ModelSerializer):
    """Class to Sede"""

    class Meta:
        model = Sede
        fields = "__all__"

class DepartamentoSerializer(serializers.ModelSerializer):
    """Class to Departamento"""

    class Meta:
        model = Departamento
        fields = "__all__"                