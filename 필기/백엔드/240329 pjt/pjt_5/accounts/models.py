from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
# 이건 클래스임. 기본 사용자 모델을 확장하기 위함

class User(AbstractUser): ##### 이거 이름 중요!!!!!!!!!!!
    pass # 이건 내일 
# AbstractUser 클래스를 상속 받은거임
 
