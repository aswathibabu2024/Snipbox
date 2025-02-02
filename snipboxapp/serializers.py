from rest_framework import serializers
from .models import Snippet, Tag

class TagSerializer(serializers.ModelSerializer):
    """serializer for tag model"""

    class Meta:
        model = Tag
        fields = '__all__'


class SnippetSerializer(serializers.ModelSerializer):
    """serializer for snippet model"""

    tags = TagSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        snippet = Snippet.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_data['title'])
            snippet.tags.add(tag)
        return snippet