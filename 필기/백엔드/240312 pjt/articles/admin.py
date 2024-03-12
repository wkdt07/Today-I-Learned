from django.contrib import admin

# Register your models here.
from .models import Post # 현재 디렉토리의 models로부터 Post 클래스를 갖고온다

admin.site.register(Post)