from rest_framework.serializers import ModelSerializer
from core.models import CarrinhoItem

class CarrinhoItemSerializer(ModelSerializer):
    class Meta:
        model = CarrinhoItem
        fields = "__all__"