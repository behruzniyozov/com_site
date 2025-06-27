from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from products.models import ProductReview
from .serializers import ReviewCreateSerializer


class ReviewCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ReviewCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            review = serializer.save()
            return Response(ReviewCreateSerializer(review).data, status=201)
        return Response(serializer.errors, status=400)
