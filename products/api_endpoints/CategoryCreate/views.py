from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Product, Category
from .serializers import CategoryCreateSerializer

class CategoryCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(
                {"message": "Category created successfully", "category_id": category.id},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
