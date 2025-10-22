from rest_framework import viewsets, permissions
from core.models import Pedido
from core.serializers import PedidoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by('-criado_em')
    serializer_class = PedidoSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        # garante que o pedido será associado ao usuário autenticado
        serializer.save(usuario=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def meus(self, request):
        qs = Pedido.objects.filter(usuario=request.user).order_by('-criado_em')
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)