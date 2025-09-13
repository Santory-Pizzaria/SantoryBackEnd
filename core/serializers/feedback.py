from rest_framework.serializers import ModelSerializer
from core.models.feedback import Feedback

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'opiniao', 'estrelas', 'criado_em']
