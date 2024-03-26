from django.shortcuts import render, redirect # 여기서 redirect까지 import 해줘야 한다.

# Create your views here.

from .models import Article # DB에 있는 모든 데이터가 나와야 하기 때문에

def index(request): # 전체 게시글
   articles = Article.objects.all()
   context = {
       'articles' : articles,
   } 
   return render(request,'articles/index.html',context) # 이래야 context까지 끌고간다

def detail(request,pk): # 단일 게시글이니깐 정보로 pk를 추가로 받아야 함
   article = Article.objects.get(pk = pk)
   context = {
       'article' : article,
   } 
   return render(request,'articles/detail.html',context) # 이래야 context까지 끌고간다

def new(request):
    return render(request,'articles/new.html')

def create(request):
    #데이터를 post 요청을 통해 전송. why? 보안상 안전하기 때문에
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 코드의 간결성: 객체를 생성하면서 동시에 속성을 설정
    article = Article(title = title, content = content) # Article의 title이 여기서 작성한 title로, Article의 content가 여기서 작성한 content도록
    # 데이터 관리의 원칙 : 안정성 --> 유효성 검사!!
    article.save()
    
    return redirect('articles:detail', article.pk) 
    # 데이터가 변경 되었을 때 해당경로로 가도록 요청

def delete(request,pk): # 특정 단일 페이지만 삭제해야 하므로 인자로 pk를 받는다
    article = Article.objects.get(pk = pk)
    article.delete()
    
    return redirect('articles:index')

def edit(request,pk): # 있던걸 수정한다는 점에서 create과 다름
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    
    return render(request,'articles/edit.html',context) # 수정하는 html로 렌더링

def update(request,pk): # create와 거의 유사, 다만 기존에 있던걸 가져와야 하니 pk를 갖고온다
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    
    # 기존에 있던걸 갖고와야 하니깐
    article = Article.objects.get(pk = pk)
    
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    
    article.save()
    
    return redirect('articles:detail', article.pk)