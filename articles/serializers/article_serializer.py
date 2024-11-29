from rest_framework import serializers
from articles.models.article import Article

class ArticleSerializer(serializers.ModelSerializer):
    """Maqolalar uchun serializer."""
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'article_type', 'author', 'created_at']
