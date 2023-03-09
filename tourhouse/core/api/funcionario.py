from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.api.serializers import FuncionarioSerializer
from rest_framework import serializers
from django.db.models import Q
from django.shortcuts import get_object_or_404

from core.models import Funcionario


class FuncionarioViewSet(viewsets.ModelViewSet):
    "Serializers handler Funcionario"
    permission_classes = (IsAuthenticated,)
    serializer_class = FuncionarioSerializer
    queryset = Funcionario.objects.all()
    filterset_fields = "__all__"
