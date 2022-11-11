from rest_framework import serializers
from articles.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('article',)

class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Comment
        fields = ('content',)
 
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comments= CommentSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Article
        fields = '__all__'
        
class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
        
    def get_user(self, obj):
        return obj.user.email
         
    def get_comments_count(self, obj):
        return obj.comments.count()
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    class Meta:
        model = Article
        fields = ('pk', 'title', 'image', 'update_at', 'user', 'comments_count', 'likes_count')

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'image', 'content')
       