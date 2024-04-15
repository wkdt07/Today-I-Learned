from django.shortcuts import render

# Create your views here.

# 이제부터 특정 html로 render 하는게 아니라 값을 줘야함
# 무슨 형태(타입)으로? JSON

from rest_framework.response import Response # 응답을 위해
from rest_framework import status # 반환할 때 상태를 확인하기 위해
from rest_framework.decorators import api_view
from .serializers import UserSerializer

@api_view(['POST']) # api에서 사용되는 view 함수이다, 특히 POST에서 사용되는
def signup(request):
    # request.data # 예전에 request.POST에 사용자가 전송한 데이터가 담겨 있는 것처럼 
    # 데코레이터 덕분에 data 안에 존재하는것
    # serializer을 통해 저장
    serializer = UserSerializer(data = request.data) # 포장 시도
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    # valid 하지 않다면
    return Response(serializer.errors)


from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import authenticate # DB에서 해당 유저가 있는지 검색
@api_view(['POST'])
def login(request):
    # serializer = UserSerializer(data = request.data)
    # if serializer.is_valid:
    #     # auth_login(request,serializer.get_user())
    username = request.data.get('username')
    password = request.data.get('password')
    # password가 암호화 되어있기 때문에 User.objects.get() 메서드로는 검색할 수 없다!
    # => authenticate 메서드를 통해 user를 검색
    user = authenticate(request,username = username, password= password)
    if user is not None:
        auth_login(request,user)
        return Response({'message' : f'{username} 로그인 성공!'})
    else:
        return Response({'error' : 'username이나 password가 잘못됨'})
    # pass


# @login_required : 기본적으로 로그인 하지 않ㅇ드면, /accounts/login/으로 보내버린다.
# 실습에서는 로그인 페이지 구현을 안했으니, 생략
@api_view(['POST'])
def logout(request):
    # 장고 내부에서 logout 로직
    # 1. 쿠키에서 session ID 삭제
    # 2. django_session 테이블에서 해당 유저 세션 정보 삭제
    message = {
        'message' : f'{request.user} 로그아웃에 성공했다!'
    }
    
    auth_logout(request)
    return Response(message,status = status.HTTP_200_OK)

from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404 # 버그 대비
from .serializers import UserArticleListSerializer
@api_view(['GET'])
def article_list(request,username):
    # username을 이용해서 해당 user 검색
    # user가 작성한 article_list 검색
    # 포장
    # 반환
    
    # username을 이용해서 해당 user 검색
    # user = get_user_model().objects.get(username = username) # 문제가 있는 코드. 뭐가 문제?
    # 내가 '존재하지 않는 유저'를 검색하면 get에서 버그가 생겨버린다. -> 사용자 입장에서는 프로그램이 갑자기 꺼져버린다. 
    # 404 에러를 뜨게 만들어야한다
    
    # get_object_or_404
    # 없는 데이터라면 404 에러를 '의도적으로' 출력하도록 함
    user = get_object_or_404(get_user_model(),username = username) # 인자는 모델과 필터링
    serializer = UserArticleListSerializer(user)
    return Response(serializer.data)
    
    pass