from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SiteConfiguration

class SiteConfigAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        config = SiteConfiguration.get_instance()
        return Response({
            "articles_per_page": config.articles_per_page,
            "allowed_file_types": config.allowed_file_types,
            "max_file_size": config.max_file_size,
        })
