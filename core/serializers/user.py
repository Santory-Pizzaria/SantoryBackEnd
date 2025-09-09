from rest_framework.serializers import ModelSerializer

from core.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'is_active', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

