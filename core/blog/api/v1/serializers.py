from rest_framework import serializers
from ...models import Post, Category
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author',  'title', 'content', 'status', 'published_date','created_date', 'updated_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']