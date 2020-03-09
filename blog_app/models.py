from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
class Article(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "user_article")
    title = models.CharField(max_length= 120, null= True, blank= True)
    content = models.CharField(max_length= 3500, null= True,blank= True)
    image = models.FileField(null= True, blank= True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE,related_name="comment")
    text = models.CharField(max_length= 120, null= True, blank= True)
    def __str__(self):
        return self.article.title + " comment"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','first_name','last_name','email','id')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )
    class Meta:
        model = Article
        fields = ('title','owner','content','id','image')
class CommentSerializer(serializers.ModelSerializer):
    article = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id',
     )
    class Meta:
        model = Comment
        fields = ('article','text')
