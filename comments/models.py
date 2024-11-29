from django.db import models
from articles.models.article import Article
from users.models.user import User

class Comment(models.Model):
    """Maqolalarga izohlar qismi uchun."""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.content[:30]}"
