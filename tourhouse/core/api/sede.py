from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.api.serializers import SedeSerializer

from core.models import Sede


class SedeViewSet(viewsets.ModelViewSet):
    "Serializers handler Sede"
    permission_classes = (IsAuthenticated,)
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    filterset_fields = "__all__"
