from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from .models import UserSerializer, Article,Comment,ArticleSerializer, CommentSerializer
@api_view(['POST'])
def register(request):
    serialized = UserSerializer(data = request.data)
    print(request.data['password'])
    data = {}
    my_email = request.data['email']
    my_username = request.data['username']
    my_password = request.data['password']
    if serialized.is_valid():
        user =User.objects.create_user(email= my_email, username= my_username, password =my_password)
        data['sucess'] = "user created"
        return Response(data = data ,status= status.HTTP_201_CREATED)
    return Response(serialized.errors, status= status.HTTP_400_BAD_REQUEST)
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def createArticle(request):
    serialized = ArticleSerializer(data= request.data)
    print(request.data)
    data = {}
    if serialized.is_valid():
        image = None
        if request.FILES:
            image = request.FILES['image']
        arti = Article(owner= request.user,title = request.data['title'], content = request.data['content'], image = image)
        arti.save()
        data['sucess'] = "article created"
        return Response(data = data ,status= status.HTTP_201_CREATED)
    return Response(serialized.errors, status= status.HTTP_400_BAD_REQUEST)
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def addComment(request, article_id):
    article = Article.objects.get(id = article_id)
    data = {}
    serialized = CommentSerializer(data= request.data)
    if serialized.is_valid():
        my_comment = Comment(article = article, text = request.data['text'])
        my_comment.save()
        data['sucess'] = "comment created"
        return Response(data = data ,status= status.HTTP_201_CREATED)
    return Response(serialized.errors, status= status.HTTP_400_BAD_REQUEST)
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def display(request):
    all_article_data = []
    all_article = Article.objects.all()
    for article in all_article:
        all_comment_article = Comment.objects.filter(article = article)
        article_comment = []
        for comment in all_comment_article:
            article_comment.append(comment.text)
        image = None
        if article.image:
            image = article.image.url
        all_article_data.append({'owner':article.owner.username,'title':article.title,'image':image,'content':article.content,'comments':article_comment})
    return HttpResponse(all_article_data)
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    data = {'message':"User logged out"}
    return Response(data = data,status=status.HTTP_200_OK)
# Create your views here.
