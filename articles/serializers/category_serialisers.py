from rest_framework import serializers
from ..models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    """
    Kategoriya ma'lumotlari  uchun serializer.
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
