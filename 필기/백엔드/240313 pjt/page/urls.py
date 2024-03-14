from django.contrib import admin
from django.urls import path, include
from . import views # 현재 디렉토리에서 views.py를 가져온다

app_name = 'page' # 이거 중요

urlpatterns = [
    path('index/',views.index, name = 'index'), # 끝자리 , 중요
]
