from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

from .forms import CommentForm
from .models import Comment
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    
    # 여기서 특정 게시글에 작성된 모든 댓글 조회(역참조)
    comments = article.comment_set.all()   
    '''
    comments = Comment.objects.all()
    이건 DB의 모든 댓글을 조회(특정 게시글에 작성된 모든 댓글 조회가 아님)
    '''
    comment_form = CommentForm() # 사용자로부터 댓글 데이터 입력을 받기 위한 form
    context = {
        'article': article,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)

def comments_create(request,pk):
    # 게시글 조회 (어떤 게시글에 작성되어야 하는지 알아야 하기 때문)
    article = Article.objects.get(pk = pk)
    
    # 사용자 입력 데이터를 받아서 comment 저장 + 유효성 검사까지
    
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comments = article.comment_set.all()   
        comment = comment_form.save(commit = False) # 데이터 저장하기 전에 임시 저장 개념
        comment.article = article
        comment.save()
        return redirect('articles:detail',article.pk)
    
    context = {
        'comment_form' : comment_form,
        'article' : article, # 얘는 article.pk를 주기 위해서
        'comments' : comments # 생성 이후에도 계속 detail에서 댓글들 보이도록
    }
    return render(request,'articles/detail.html',context)
    
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

def comments_delete(request,article_pk,comment_pk):
    # 어떤 댓글을 삭제할지 조회
    
    comment = Comment.objects.get(pk = comment_pk)
    # 사실 article_pk = comment.article.pk라고 하면 굳이 valuable 하나 더 안 써도 되지만 지금까지 urls에서 valuable routing 하면서 사용한 전체적인 구조의 통일성을 위해서 (detail 조회/ comment 조회)
    # 이게 가능한 이유는 '참조' 때문
    
    comment.delete()
    
    return redirect('articles:detail',article_pk)