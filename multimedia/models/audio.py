from django.db import models

class Audio(models.Model):
    """Audiolar  uchun model."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='audios/')
    duration = models.DurationField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
