from rest_framework import serializers

from users.models import UserModel


class UserSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(required=False)
    bio = serializers.CharField(required=False)
    avatar = serializers.ImageField(required=False)

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
