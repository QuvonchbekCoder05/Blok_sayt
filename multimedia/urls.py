from django.urls import path
from .views import VideoView,AudioListAPIView,ImageListAPIView

urlpatterns = [
    path('videos/', VideoView.as_view(), name='video-list'),
    path('audios/', AudioListAPIView.as_view(), name='audio-list'),
    path('images/', ImageListAPIView.as_view(), name='image-list'),
]
