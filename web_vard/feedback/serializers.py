from rest_framework import serializers

from .models import Feedback
from user.models import User


class FeedbackSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_creation = serializers.DateTimeField(read_only=True)
    theme = serializers.CharField(max_length=255)
    description = serializers.CharField()

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.theme = validated_data.get('theme', instance.theme)
        instance.description = validated_data.get('comment', instance.description)
        instance.save()

        return instance
