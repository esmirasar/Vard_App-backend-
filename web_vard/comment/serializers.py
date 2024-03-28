from rest_framework import serializers


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
