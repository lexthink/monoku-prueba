from apps.users.api.permissions import IsAdmin, CanEditOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import CanBeTaken
from .serializers import ProductSerializer, OptionSerializer
from ..models import Product, Option


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, CanEditOrReadOnly)

    @action(detail=True)
    def options(self, request, pk):
        product = self.get_object()
        serializer = OptionSerializer(product.get_options(), many=True, context={'request': request})
        return Response(serializer.data)


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = (IsAuthenticated, CanEditOrReadOnly)

    @action(detail=True, methods=['post', 'get'], permission_classes=[IsAuthenticated, CanBeTaken])
    def take(self, request, pk):
        option = self.get_object()
        return Response({'taken': request.user.take(option)})
