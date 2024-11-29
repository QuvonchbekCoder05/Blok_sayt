from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Article(models.Model):
    """Maqolalar uchun model."""
    ARTICLE_TYPES = [
        ('simple', 'Oddiy Maqola'),
        ('technical', 'Texnik Maqola'),
        ('news', 'Yangiliklar'),
    ]
    title = models.CharField(max_length=255)  # Maqola sarlavhasi
    content = models.TextField()  # Maqola matni
    article_type = models.CharField(max_length=50, choices=ARTICLE_TYPES)  # Maqola turi
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')  # Muallif
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana

    def __str__(self):
        return f"{self.title} - {self.article_type}"
