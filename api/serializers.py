from rest_framework import serializers
from web.models import Article, ArticleCategory
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    author = UserSerializer('username')

    class Meta:
        model = Article
        exclude = ['created', 'is_special']
