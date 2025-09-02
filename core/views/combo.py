from rest_framework import viewsets
from core.models import Combo
from core.serializers.combo import ComboSerializer

class ComboViewSet(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer