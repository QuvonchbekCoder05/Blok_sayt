from rest_framework import serializers
from multimedia.models.audio import Audio

class AudioSerializer(serializers.ModelSerializer):
    """Audiolar uchun serializer."""
    class Meta:
        model = Audio
        fields = ['id', 'title', 'description', 'file', 'duration', 'uploaded_at']
