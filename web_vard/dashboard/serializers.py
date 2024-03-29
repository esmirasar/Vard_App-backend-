from rest_framework import serializers

from .models import Dashboard
from user.models import User


class DashboardSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_creation = serializers.DateTimeField(read_only=True)
    date_change = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Dashboard.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.save()

        return instance
