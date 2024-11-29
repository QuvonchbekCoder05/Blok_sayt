from rest_framework import serializers
from ..models.tag import Tag

class TagSerializer(serializers.ModelSerializer):
    """
    Teg ma'lumotlari uchun serializer.
    """
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at']
