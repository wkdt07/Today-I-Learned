from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 기본적으로 MTM 필드는 복수형으로 쓴다
    followings = models.ManyToManyField('self', symmetrical= False, related_name = 'followers')# 팔로잉 -> 내가 누군가를 참조하는것, 팔로잉과 팔로워 생각. 기준은 '나'

# 만약 related_name 설정을 안 하면?
## 정참조(내가 팔로우하고 있는 사람들) : user1.followings.all()
## 역참조(나를 팔로우하고 있는 사람들) : user2.user_set.all()

# manytomany의 가장 큰 특징? 모델을 직접적으로 바꾸는게 아니라 '중개테이블을 만든다'