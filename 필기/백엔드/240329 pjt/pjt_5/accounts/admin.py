from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
# UserAdmin : 사용자 모델 관리자, 장고의 기본 디폴트. 

from .models import User # 클래스명 반드시 이걸로 지어야 한다. 
# why? settings에서 AUTO_USER_MODEL = 'accounts.User' 했음

admin.site.register(User,UserAdmin) # UserAdmin을 통해 User를 사용하겠다.