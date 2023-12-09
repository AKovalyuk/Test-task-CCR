from rest_framework import serializers

from news.models import Post
from utils import rescale


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['preview_image']

    def create(self, validated_data):
        obj = Post.objects.create(**validated_data)
        obj.preview_image.save(
            name=obj.main_image.name,
            content=rescale(obj.main_image, 200),
        )
        return obj

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        instance.preview_image.save(
            name=instance.main_image.name,
            content=rescale(instance.main_image, 200),
        )
        instance.save()
        return instance
