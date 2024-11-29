from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from articles.models.article import Article
from articles.models.tag import Tag
from articles.models.category import Category
from articles.serializers.article_serializer import ArticleSerializer
from articles.serializers.category_serialisers import CategorySerializer
from articles.serializers.tag_serializers import TagSerializerSerializer

class ArticleView(APIView):
    """Maqolalar uchun API view."""
    def get(self, request):
        """Barcha maqolalarni olish."""
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Yangi maqola qo'shish."""
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagListCreateAPIView(generics.ListCreateAPIView):
    """
    Teglar ro'yxatini olish va yangi teg yaratish uchun API.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Tegni olish, yangilash va o'chirish uchun API.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    Kategoriyalar ro'yxatini olish va yangi kategoriya yaratish uchun API.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Kategoriyani olish, yangilash va o'chirish uchun API.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
