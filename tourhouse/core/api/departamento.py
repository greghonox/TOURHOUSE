from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.api.serializers import DepartamentoSerializer
from django.db.models import Q

from core.models import Departamento


class DepartamentoViewSet(viewsets.ModelViewSet):
    "Serializers handler Departamento"
    permission_classes = (IsAuthenticated,)
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()
    filterset_fields = "__all__"

    def _build_query_parameters(self):
        centro_custo = self.request.GET.get('centro_custo')
        codigo_integracao = self.request.GET.get('codigo_integracao')
        fields = [centro_custo, codigo_integracao]
        if any([query for query in fields]):
            filters = Q()
            if centro_custo:
                filters &= Q(centro_custo=centro_custo)
            if codigo_integracao:
                filters &= Q(codigo_integracao=codigo_integracao)
            return filters
        else:
            return {}
        
    def list(self, request):
        parameters = self._build_query_parameters()
        if parameters != {}:
            departamentos = Departamento.objects.filter(parameters)
        else:
            departamentos = Departamento.objects.all()
        serializer = self.serializer_class(departamentos, many=True)
        return Response(serializer.data, 200)