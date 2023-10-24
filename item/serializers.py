from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Item
        fields = ('id','name', 'price', 'description')