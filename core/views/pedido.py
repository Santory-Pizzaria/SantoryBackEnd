from rest_framework import viewsets
from core.models import Pedido
from core.serializers import PedidoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by('-criado_em')
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # garante que o pedido será associado ao usuário autenticado
        serializer.save(usuario=self.request.user)

    @action(detail=False, methods=['get'])
    def me(self, request):
        """Retorna o usuário autenticado"""
        user = request.user
        if not user.is_authenticated:
            return Response({'detail': 'Usuário não autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='meus-pedidos')
    def meus_pedidos(self, request):
        pedidos = Pedido.objects.filter(usuario=request.user)
        serializer = self.get_serializer(pedidos, many=True)
        return Response(serializer.data)


class PedidoUsuarioListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pedidos = Pedido.objects.filter(usuario=request.user)
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)