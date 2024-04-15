"""
URL configuration for pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

# accounts
# 1. 회원가입(POST) -> user 생성
# 2. 로그인(POST) -> session 생성, session? 로그인 된 정보를 유지하는 방법. 쿠키 같은거
# 3. 로그아웃(POST) -> session 삭제
# 6. 유저가 작성한 articles(GET)

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup, name = 'signup'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    # path('<str:username>/',views.article_list, name = 'article_list'),
    # path('<str:username>/articles/',views.article_list, name = 'article_list'), # 이거까지 표현하는게 더 좋은 URI(직관적)
]
