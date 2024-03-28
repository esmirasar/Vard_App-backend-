from rest_framework import serializers
from chart.models import Chart


class ChartSerializer(serializers.Serializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_creation = serializers.DateTimeField(read_only=True)
    date_change = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Chart.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.save()

        return instance