from rest_framework import viewsets
from core.models import Feedback
from core.serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('-criado_em')
    serializer_class = FeedbackSerializer
