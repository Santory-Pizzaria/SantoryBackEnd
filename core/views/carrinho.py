from rest_framework import viewsets
from core.models import Carrinho
from core.serializers.carrinho import CarrinhoSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
