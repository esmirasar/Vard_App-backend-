from rest_framework import serializers

from .models import Access, AccessType
from file.models import File
from user.models import User


class AccessSerializer(serializers.Serializer):

    file = serializers.PrimaryKeyRelatedField(queryset=File.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    access_type = serializers.PrimaryKeyRelatedField(queryset=AccessType.objects.all())
    date_access_open = serializers.DateTimeField(read_only=True)
    date_access_close = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Access.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.file = validated_data.get('file', instance.file)
        instance.access_type = validated_data.get('access_type', instance.access_type)
        instance.save()

        return instance
