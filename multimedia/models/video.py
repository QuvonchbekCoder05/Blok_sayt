from django.db import models

class Video(models.Model):
    """Videolar uchun model."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    duration = models.DurationField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
