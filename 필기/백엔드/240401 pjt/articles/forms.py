from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#   title = forms.CharField(max_length=10)
#   content = forms.CharField(widget = forms.Textarea)

# form 과 modelform의 차이??
# 사용자로 부터 입력을 받은 것을 DB에 저장하는지 안 하는지 차이

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article # 이 폼이 사용할 모델을 Article
    fields = '__all__' # Article 모델의 모든 필드를 폼에 사용하겠다.