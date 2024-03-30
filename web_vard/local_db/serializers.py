from rest_framework import serializers

from .models import Connection
from user.models import User


class ConnectionSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    password = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    driver = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    url = serializers.URLField(max_length=255, allow_null=True, allow_blank=True)
    host = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    port = serializers.IntegerField(allow_null=True)
    data_base_type = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    name = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    description = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    connection = serializers.BooleanField()

    def create(self, validated_data):
        return Connection.objects.create(**validated_data)
