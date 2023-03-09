from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.api.serializers import FuncionarioSerializer

from core.models import Funcionario


class FuncionarioViewSet(viewsets.ModelViewSet):
    "Serializers handler Funcionario"
    permission_classes = (IsAuthenticated,)
    serializer_class = FuncionarioSerializer
    queryset = Funcionario.objects.all()
    filterset_fields = "__all__"
