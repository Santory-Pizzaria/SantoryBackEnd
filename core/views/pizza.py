from rest_framework import viewsets
from core.models import Pizza
from core.serializers.pizza import PizzaSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer