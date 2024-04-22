from rest_framework import serializers

from .models import User, Token


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    date_creation = serializers.DateTimeField(read_only=True)
    date_password_change = serializers.DateTimeField(read_only=True)

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


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=25, allow_null=True, allow_blank=True)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Token.objects.create(**validated_data)

