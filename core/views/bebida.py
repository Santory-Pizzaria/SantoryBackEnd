from rest_framework import viewsets
from core.models import Bebida
from core.serializers.bebida import BebidaSerializer

class BebidaViewSet(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer
