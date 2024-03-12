from django.contrib import admin
from django.urls import path,include
from . import views # 현재 디렉토리에서 views를 갖고온다

urlpatterns = [
    path('',views.index)
    # index라는 함수를 views에 만들어야 한다. 
    # 이제 index.html을 만들어야 한다. 어디에? templates에. 없으면 templates라는 폴더를 앱 안에 만들고, 그 안에 앱 이름과 같은 폴더를 하나 더 만든다. 
]