from rest_framework import viewsets
from core.models import CarrinhoItem
from core.serializers.carrinhoItem import CarrinhoItemSerializer

class CarrinhoItemViewSet(viewsets.ModelViewSet):
    queryset = CarrinhoItem.objects.all()
    serializer_class = CarrinhoItemSerializer