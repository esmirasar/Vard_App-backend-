from rest_framework import serializers

from .models import Comment, ReadComment
from chart.models import Chart
from dashboard.models import Dashboard
from file.models import File
from user.models import User


class CommentSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    file = serializers.PrimaryKeyRelatedField(queryset=File.objects.all())
    chart = serializers.PrimaryKeyRelatedField(read_only=True)
    dashboard = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_send = serializers.DateTimeField(allow_null=True)
    date_remove = serializers.DateTimeField(default=None)
    date_delivery = serializers.DateTimeField(allow_null=True)
    comment = serializers.CharField(allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.comment = validated_data.get('description', instance.comment)
        instance.save()

        return instance


class ReadCommentSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())
    date_reading = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return ReadComment.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()

        return instance
