from rest_framework import serializers

from .models import File, Place, FileType
from user.models import User


class FileSerializer(serializers.Serializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=FileType.objects.all())
    date_creation = serializers.DateTimeField(read_only=True)
    date_change = serializers.DateTimeField(read_only=True)
    date_delete = serializers.DateTimeField(read_only=True)
    name = serializers.CharField(max_length=255)
    link = serializers.URLField(max_length=255)
    publish = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return File.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.place = validated_data.get('place', instance.place)
        instance.name = validated_data.get('name', instance.name)
        instance.link = validated_data.get('link', instance.link)
        instance.publish = validated_data.get('publish', instance.publish)
        instance.save()

        return instance
