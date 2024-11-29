from django.urls import path
from .views import (
    ArticleView,
    TagListCreateAPIView,
    TagRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Maqolalar uchun API
    path('articles/', ArticleView.as_view(), name='article-list-create'),
    
    # Teglar uchun API
    path('tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-retrieve-update-destroy'),

    # Kategoriyalar uchun API
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
]