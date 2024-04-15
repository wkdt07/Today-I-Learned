from rest_framework import serializers
from .models import Article

from django.contrib.auth import get_user_model
class ArticleLisetSerializer(serializers.ModelSerializer):
    # 만약 user를 다르게 나타내고 싶으면
    
    # 예시 1. user의 nickname으로 
    # user 필드의 출력 애용을 재정의
    # source : 어떤 내용을 출력할 것인가
    # user = serializers.CharField(source = 'user.nickname') # 포장을 재정의 
    
    
    # 예시 2. user의 필드를 전부 출력
    # ## 그럼 모든 user를 필드에 다 출력하고 싶으면?
    
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = get_user_model()
    #         fields = '__all__'
            
    
    # user = UserSerializer()
    
    class Meta:
        model = Article
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer): # POST용
    class Meta:
        model = Article
        fields = ('title','content',)