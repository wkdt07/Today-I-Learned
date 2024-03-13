from django.contrib import admin
from django.urls import path, include
from . import views # 현재 디렉토리에서 views.py를 가져온다

app_name = 'articles' # 이거 중요

urlpatterns = [
    path('index/',views.index,name = 'index'), # 끝자리 , 중요
    path('dinner/',views.dinner,name = 'dinner'),
    path('search/',views.search,name = 'search'),
    path('throw/',views.throw,name = 'throw'),
    path('catch/',views.catch,name = 'catch'),
    path('articles/<int:num>',views.detail),# num이란 변수가 int로 받아야한다.
]
