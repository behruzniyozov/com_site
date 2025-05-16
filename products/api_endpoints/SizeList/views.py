from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Size
from .serializers import SizeListSerializer



class SizeListView(APIView):
    permission_classes = []

    def get(self, request):
        sizes = Size.objects.all()
        serializer = SizeListSerializer(sizes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)