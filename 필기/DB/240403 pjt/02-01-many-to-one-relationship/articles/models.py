from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model): # 댓글의 클래스
    # 둘의 관계 만들기
    article = models.ForeignKey(Article,on_delete = models.CASCADE)# 인스턴스는 참조하는 모델의 단수형으로 하는걸 권장
    # on_delete는 참조하는 객체(게시글)가 지워졌을 때의 처리법
    # 댓글이 달리면 삭제를 금지하게 할 수도, 아니면 다같이 지워지게 할 수도(이거) 있다. 
    # 그리고 이거 위치 상관 없는게, 어차피 ForeignKey 특성으로 맨 오른쪽으로 이동됨
    content = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    