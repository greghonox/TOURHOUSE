from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.api.serializers import SedeSerializer
from rest_framework.response import Response
from django.db.models import Q
from core.models import Sede


class SedeViewSet(viewsets.ModelViewSet):
    "Serializers handler Sede"
    permission_classes = (IsAuthenticated,)
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    filterset_fields = "__all__"

    def _build_query_parameters(self):
        cnpj = self.request.GET.get('cnpj')
        logradouro = self.request.GET.get('logradouro')
        cidade = self.request.GET.get('cidade')
        pais = self.request.GET.get('pais')
        fields = [cnpj, logradouro, cidade, pais]
        if any([query for query in fields]):
            filters = Q()
            if cnpj:
                filters &= Q(cnpj__contains=cnpj)
            if logradouro:
                filters &= Q(logradouro__contains=logradouro)
            if cidade:
                filters &= Q(cidade__contains=cidade)
            if pais:
                filters &= Q(pais__contains=pais)
            return filters
        else:
            return {}
        
    def list(self, request):
        parameters = self._build_query_parameters()
        if parameters != {}:
            sede = Sede.objects.filter(parameters)
        else:
            sede = Sede.objects.all()
        serializer = self.serializer_class(sede, many=True)
        return Response(serializer.data, 200)