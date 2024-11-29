from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

class CommentView(APIView):
    """Izohlarni boshqarish qismi"""
    def get(self, request, article_id):
        """Maqoladagi izohlarni olish ."""
        comments = Comment.objects.filter(article_id=article_id, is_approved=True)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_id):
        """Yangi izoh qo'shish."""
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, article_id=article_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
