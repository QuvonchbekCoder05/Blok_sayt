from rest_framework import serializers
from users.models.user import User

class UserSerializer(serializers.ModelSerializer):
    """Foydalanuvchilar uchun serializer."""
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'is_active', 'is_staff']
