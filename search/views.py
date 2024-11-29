from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import F
from .models import SearchTerm
from .serializers import SearchTermSerializer

class SearchAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.query_params.get('q', '')  # Qidiruv so'zi query orqali 
        if query:
            search_term, created = SearchTerm.objects.get_or_create(term=query)
            if not created:
                search_term.count = F('count') + 1  # Qidiruv sonini oshirib boramiz 
                search_term.save(update_fields=['count'])

            related_terms = SearchTerm.objects.filter(term__icontains=query).order_by('-count')[:5]
        else:
            related_terms = SearchTerm.objects.none()

        serializer = SearchTermSerializer(related_terms, many=True)
        return Response(serializer.data)
