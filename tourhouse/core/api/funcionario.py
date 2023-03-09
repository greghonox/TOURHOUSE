from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.api.serializers import FuncionarioSerializer
from django.db.models import Q

from core.models import Funcionario


class FuncionarioViewSet(viewsets.ModelViewSet):
    "Serializers handler Funcionario"
    permission_classes = (IsAuthenticated,)
    serializer_class = FuncionarioSerializer
    queryset = Funcionario.objects.all()
    filterset_fields = "__all__"

    def _build_query_parameters(self):
        nome_completo = self.request.GET.get('nome_completo')
        email = self.request.GET.get('email')
        telefone = self.request.GET.get('telefone')
        data_nascimento = self.request.GET.get('data_nascimento')
        data_ingresso = self.request.GET.get('data_ingresso')
        data_desligamento = self.request.GET.get('data_desligamento')
        ativo = self.request.GET.get('ativo')
        cidade = self.request.GET.get('cidade')
        departamento_sede = self.request.GET.get('departamento_sede')
        fields = [nome_completo, email, telefone, data_nascimento, 
                  data_ingresso, data_desligamento, ativo, cidade, departamento_sede]
        if any([query for query in fields]):
            filters = Q()
            if nome_completo:
                filters &= Q(nome_completo__contains=nome_completo)
            if email:
                filters &= Q(email__contains=email)
            if telefone:
                filters &= Q(telefone__contains=telefone)
            if data_nascimento:
                filters &= Q(data_nascimento__contains=data_nascimento)
            if data_ingresso:
                filters &= Q(data_ingresso__contains=data_ingresso)
            if data_desligamento:
                filters &= Q(data_desligamento__contains=data_desligamento)
            if ativo:
                filters &= Q(ativo__contains=ativo)
            if cidade:
                filters &= Q(cidade__contains=cidade)
            if departamento_sede:
                filters &= Q(departamento_sede__contains=departamento_sede)
            return filters
        else:
            return {}
        
    def list(self, request):
        parameters = self._build_query_parameters()
        if parameters != {}:
            funcionarios = Funcionario.objects.filter(parameters)
        else:
            funcionarios = Funcionario.objects.all()
        serializer = self.serializer_class(funcionarios, many=True)
        return Response(serializer.data, 200)