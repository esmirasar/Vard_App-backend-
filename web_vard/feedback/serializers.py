from rest_framework import serializers
from feedback.models import Feedback


class FeedbackSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_creation = serializers.DateTimeField(read_only=True)
    theme = serializers.CharField(max_length=255)
    description = serializers.CharField()

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.theme = validated_data.get('theme', instance.theme)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance
