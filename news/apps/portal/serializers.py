from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS
from .models import (Author,
                     Category,
                     Organization,
                     Tag,
                     Post)


# Organizations model serializers
# Serializer for method "GET"
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ALL_FIELDS


# Serializer for create-update methods
class OrganizationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        exclude = ('id', 'slug',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ALL_FIELDS


class TagPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('id', 'slug',)


class AuthorSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Author
        fields = ALL_FIELDS


class AuthorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ALL_FIELDS
        exclude = ('id', 'slug',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ALL_FIELDS


class CategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id', 'slug',)


class PostsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    authors = AuthorSerializer(many=True)
    category = CategorySerializer(many=False)

    class Meta:
        model = Post
        fields = ALL_FIELDS


class PostsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ALL_FIELDS
        exclude = ('slug',
                   'id',
                   'created_at',
                   'updated_at',
                   'views',
                   )
