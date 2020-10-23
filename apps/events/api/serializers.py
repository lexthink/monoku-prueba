from rest_framework import serializers
from ..models import Event, Stand


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name',)


class StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stand
        fields = ('id', 'event', 'name',)
