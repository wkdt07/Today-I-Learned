from django import forms # 장고의 forms 모듈부터 갖고 와야 django form을 만들 수 있음

# class ArticleForm(forms.Form): # 장고의 Form을 상속받아서 새로운 폼 작성
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) # 크기 조절이 가능하도록 위젯 사용
    
# 사실 일반 폼이 아니라 modelform을 사용해야함

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # 갖고오고 싶은 모델이 있다. 걔를 적용할거. 근데 사용하려면? import를 해줘야함
        fields = '__all__' # 필드는 내가 갖고 오고 싶은 테이블 내 행의 종류.(데이터 종류), 여기서 '__all__'은 싹 다 갖고오라는 뜻
        # widget을 적용하고 싶다? 강의자료의 widget 응용 확인
        