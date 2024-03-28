from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(blank=True) # blank=True는 이미지 업로드 안 하고 데이터 추가했을 때 오류 방지용, img 가 비어있어도 된다.
    # image = models.ImageField(blank=True,upload_to='images/')
    # upload_to='images/' -> 업로드된 이미지 파일들이 MEDIA_ROOT의 하위 디렉토리 'images/'에 저장
    
    image = models.ImageField(blank=True,upload_to='%Y/%M/%d/')
    # 업로드 된 파일을 서버상에서 날짜별로 분류해서 저장해라q