from rest_framework import serializers
from multimedia.models.video import Video

class VideoSerializer(serializers.ModelSerializer):
    """Videolar uchun serializer."""
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'duration', 'uploaded_at']
