from django.contrib import admin
from .models.article import Article
from .models.tag import Tag
from .models.category import Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'author', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('type', 'created_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
