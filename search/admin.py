from django.contrib import admin
from .models import SearchTerm

@admin.register(SearchTerm)
class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('id', 'term', 'count')
    search_fields = ('term',)
