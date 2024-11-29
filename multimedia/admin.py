from django.contrib import admin
from .models.video import Video
from .models.image import Image
from .models.audio import Audio

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'duration', 'uploaded_at')
    search_fields = ('title', 'description')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'uploaded_at')
    search_fields = ('title',)

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'duration', 'uploaded_at')
    search_fields = ('title',)
