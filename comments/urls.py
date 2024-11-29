from django.urls import path
from comments.views import CommentView

urlpatterns = [
    path('articles/<int:article_id>/comments/', CommentView.as_view(), name='article-comments'),
]
