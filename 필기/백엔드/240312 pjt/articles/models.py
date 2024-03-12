# 데이터 베이스를 관리하는 부분

from django.db import models

# Create your models here.

#models.Model : DB의 테이블 (엑셀 테이블 같은거)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) # 자동 생성
    
    def __str__(self):
        # 우리 눈에 보이는 게시글은 pk(id:고유번호)와 title로 구성
        return f'[{self.pk} {self.title}]' 
        #pk는 고유아이디. 1번부터 시작. 삭제한다고 다시 돌아가지 않음