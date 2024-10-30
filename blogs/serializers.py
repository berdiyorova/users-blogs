from rest_framework import serializers

from blogs.models import BlogModel, CommentModel
from users.models import UserModel


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    def create(self, validated_data):
        return BlogModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    def create(self, validated_data):
        return CommentModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
