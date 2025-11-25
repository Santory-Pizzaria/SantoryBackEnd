from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import Reserva
from core.serializers.reserva import ReservaSerializer

class ReservaUsuarioListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reservas = Reserva.objects.filter(usuario=request.user)
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer