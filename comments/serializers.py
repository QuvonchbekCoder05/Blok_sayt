from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """Izohlar uchun serializer."""
    class Meta:
        model = Comment
        fields = ['id', 'article', 'author', 'content', 'is_approved', 'created_at']
