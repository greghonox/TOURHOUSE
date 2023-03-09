from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.api.serializers import DepartamentoSerializer

from core.models import Departamento


class DepartamentoViewSet(viewsets.ModelViewSet):
    "Serializers handler Departamento"
    permission_classes = (IsAuthenticated,)
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()
    filterset_fields = "__all__"
