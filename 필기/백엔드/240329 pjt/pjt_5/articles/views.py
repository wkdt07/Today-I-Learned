from django.shortcuts import render, redirect

# Create your views here.
from .models import Article

from .forms import ArticleForm

def index(request): # 전체 게시글 조회
  articles = Article.objects.all()
  context = {
    'articles' : articles,
  }
  return render(request, 'articles/index.html', context)

def detail(request, pk): #단일 게시글 조회
  article = Article.objects.get(pk = pk)
  context = {
    'article' : article,
  }
  return render(request, 'articles/detail.html', context)

# def new(request):
#   return render(request, 'articles/new.html')

# def create(request):
#   # 데이터를 POST요청을 통해 서버로 전송 - 보안상 안전하기 때문에
#   title = request.POST.get('title')
#   content = request.POST.get('content')

#   # 코드의 간결성 : 객체를 생성하면서 동시에 속성을 설정
#   article = Article(title = title, content = content)
#   # 테이터 관리의 원칙 : 안정성 ---> 유효성 검사!!
#   article.save()

#   return redirect('articles:detail', article.pk)
#   # 데이터 변경 되었을 때 경로에 요청

# 1. 사용자가 폼 페이지를 처음 방문(GET요청), 비어있는 폼을 랜더링 사용자가 데이터를 입력할 수 있게
# 2. 폼을 제출하면(POST요청), 제출된 데이터로 인스턴스 생성
# 3. 유효성 검사 후, 유효하면 DB에 저장, 사용자를 상세 페이지로 리다이렉트
# 1-1. 제출버튼을 누르지 않은 경우(POST요청이 아닌경우) 모든 필드가 비어 있는 상태로 사용자에게 보여지게

def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    # 1. 모든 필수 필드가 채워져 있다.
    # 2. 입력된 데이터가 필드의 조건(ex 데이터 형식)을 만족해야 한다.
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm()
    
  context = {
    'form' : form,
  }
  return render(request, 'articles/create.html', context)

def update(request, pk):
  article = Article.objects.get(pk = pk)

  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
  else:
    # 기존 데이터를 form instace에 넣어준다.
    form = ArticleForm(instance=article)

  context = {
    'article' : article,
    'form' : form,
  }

  return render(request, 'articles/update.html', context)


def delete(request, pk):
  article = Article.objects.get(pk = pk)
  article.delete()

  return redirect('articles:index')

# def edit(request, pk):
#   article = Article.objects.get(pk = pk)
#   context = {
#     'article' : article,
#   }
#   return render(request, 'articles/edit.html', context)

# def update(request, pk):
#   article = Article.objects.get(pk = pk)

#   article.title = request.POST.get('title')
#   article.content = request.POST.get('content')

#   article.save()

#   return redirect('articles:detail', article.pk)

