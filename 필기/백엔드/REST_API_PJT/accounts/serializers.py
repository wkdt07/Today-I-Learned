from rest_framework import serializers
from django.contrib.auth import get_user_model


# form 쓸 때랑 똑같다!
# forms.Form 과 forms.ModelForm

# class UserSerializer(serializers.ModelSerializer): # 모델에 있는것만 받을거면  ModelsSerializer, 이외에도 받을게 있으면 그냥 Serializer
#     class Meta:
#         model = get_user_model()
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer): # 모델에 있는것만 받을거면  ModelsSerializer, 이외에도 받을게 있으면 그냥 Serializer
    class Meta:
        model = get_user_model()
        fields = ('username','password', 'nickname',)

    # 암호화를 위해
    def create(self,validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user



from articles.models import Article
class UserArticleListSerializer(serializers.ModelSerializer):
    # 역참조를 이용해서 user가 작성한 article_list를 추가할 수 있다
    
    # 1. article은 title,content 등 데이터가 여러 개
    # -> nested serializer를 정의
    # Article 모델을 가져와서
    
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = '__all__'
    
    # 2. field에 추가
    article_set = ArticleSerializer(many = True) # 데이터가 여러개로, 리스트로 묶인 형태이니깐 
    # 항상 Model이 '아는 필드 명'으로 작성을 해주어야 한다! (여기선 User)
    # 역참조 이름을 알기 때문에, 아래 변수 이름은 반드시 article_set
    class Meta:
        model = get_user_model()
        # 3. 실질적 추가
        # 위에서 작성한 필드 추가 안 해주면 버그 발생! (이건 문법)
        fields = ('username','nickname','article_set',)