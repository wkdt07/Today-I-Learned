from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleLisetSerializer,ArticleSerializer
# from django.contrib.auth import get_user_model
from accounts.models import User
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            # user 필드를 지정해줘야 한다. (foreign key)
            serializer.save(user = request.user)
            return Response(serializer.data)
        
        # 데이터가 제대로 안 들어갔을 때 반환
        else: 
            return Response(serializer.errors)
            
    
    # 이거 먼저
    elif request.method == 'GET': #그냥 else로 적어도 됨
        # DB에서 articles 전체 조회
        # JSON으로 포장
        # return 
        articles = Article.objects.all()
        # 포장하려면 시리얼라이저 필요
        # all은 2개 이상일 수 있다(리스트 형태로 반환)
        # -> 포장할 때, many = True 옵션을 주어야 한다.
        
        serializer = ArticleLisetSerializer(articles, many = True) # all()은 2개 이상일 수 있으니깐
        
        return Response(serializer.data)
        
    pass
