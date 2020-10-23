from apps.users.api.permissions import IsAdmin, CanEditOrReadOnly
from apps.products.api.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EventSerializer, StandSerializer
from ..models import Event, Stand


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, IsAdmin, CanEditOrReadOnly)

    @action(detail=True)
    def stands(self, request, pk):
        event = self.get_object()
        serializer = StandSerializer(event.stands, many=True, context={'request': request})
        return Response(serializer.data)


class StandViewSet(viewsets.ModelViewSet):
    queryset = Stand.objects.all()
    serializer_class = StandSerializer
    permission_classes = (IsAuthenticated, CanEditOrReadOnly)

    @action(detail=True)
    def products(self, request, pk):
        stand = self.get_object()
        serializer = ProductSerializer(stand.products, many=True, context={'request': request})
        return Response(serializer.data)
