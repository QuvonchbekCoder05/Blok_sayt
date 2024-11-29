from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'author', 'article', 'created_at', 'is_approved')
    search_fields = ('content', 'author__username', 'article__title')
    list_filter = ('is_approved', 'created_at')
