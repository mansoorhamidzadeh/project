from rest_framework import serializers
from web.models import Article, ArticleCategory
from django.contrib.auth.models import User


class UserSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.username

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ['title']


class ArticleSerializer(serializers.ModelSerializer):
    # def get_author(self,obj):
    #     return obj.author.username
    #author = serializers.SerializerMethodField('get_author')
    #category = serializers.SlugRelatedField(many=True, slug_field='title', queryset=ArticleCategory.objects.all())
    category=CategorySerializer(many=True,read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'author',
            'title',
            'content',
            'category',
            'published',
            'created',
            'is_special',
            'status',
        ]
    #