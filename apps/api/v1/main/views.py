from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.v1.main.models import KunUzNews
from apps.api.v1.main.serializers import KunUzNewsReadSerializer


@api_view(['GET'])
def news_list(request: HttpRequest) -> HttpResponse:
    return Response(
        KunUzNewsReadSerializer(KunUzNews.objects.all(), many=True).data,
        status=200
    )
