from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): # UserCreationForm의 메타를 상속받은거
        model = get_user_model()
        



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name','last_name','email') # 변경 할 필드 설정