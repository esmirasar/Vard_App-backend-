from rest_framework import serializers

from models.models import (User, File, Place, FileType, AccessType, Access,
                           Feedback, Chart, Dashboard, Comment, ReadComment)


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    date_creation = serializers.DateTimeField(read_only=True)
    date_passwords_change = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):

        password = instance.password

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password')

        if instance.password:
            instance.set_password(instance.password)
        else:
            instance.password = password

        instance.save()

        return instance


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


class DashboardSerializer(serializers.Serializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_creation = serializers.DateTimeField(read_only=True)
    date_change = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Dashboard.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.save()

        return instance


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


class CommentSerializer(serializers.Serializer):

    file = serializers.PrimaryKeyRelatedField(queryset=File.objects.all())
    chart = serializers.PrimaryKeyRelatedField(queryset=Chart.objects.all())
    dashboard = serializers.PrimaryKeyRelatedField(queryset=Dashboard.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_send = serializers.DateTimeField(read_only=True)
    date_remove = serializers.DateTimeField(read_only=True)
    date_delivery = serializers.DateTimeField(read_only=True)
    comment = serializers.CharField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.file = validated_data.get('file', instance.file)
        instance.dashboard = validated_data.get('dashboard', instance.dashboard)
        instance.chart = validated_data.get('chart', instance.chart)
        instance.comment = validated_data.get('comment', instance.comment)

        instance.save()

        return instance


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


class ReadCommentSerializer(serializers.Serializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())
    date_reading = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return ReadComment.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.comment = validated_data.get('comment', instance.comment)

        instance.save()

        return instance


class ChartSerializer(serializers.Serializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_creation = serializers.DateTimeField(read_only=True)
    date_change = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Chart.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.save()

        return instance
