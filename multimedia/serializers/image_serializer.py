from rest_framework import serializers
from multimedia.models.image import Image

class ImageSerializer(serializers.ModelSerializer):
    """Rasmlar uchun serializer."""
    class Meta:
        model = Image
        fields = ['id', 'title', 'description', 'file', 'uploaded_at']
