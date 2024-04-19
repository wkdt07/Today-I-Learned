from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)




def logout(request):
    auth_logout(request)
    return redirect('boards:index')

from django.contrib.auth import get_user_model
from boards.models import Comment,Board

@login_required
def profile(request,user_pk):
    me = get_user_model().objects.get(pk = user_pk)
    comments = Comment.objects.filter(author_id = user_pk)
    boards = Board.objects.filter(author_id = user_pk)
    followers = me.followers.all()

    context = {
        'me' : me,
        'nickname' : me.username,
        'followings' : me.followings.all(),
        'comments' : comments,
        'boards' : boards,
        'followers' : followers,
        'user_pk' : user_pk
    }
    return render(request,'accounts/profile.html',context)
# from .models import User

# 팔로우버튼은 상대방 프로필페이지에서
@login_required
def follow(request,user_pk):
    # user_pk는 내가 디테일 함수에서 확인할 수 있는 user_pk-> 상대방
    # 어차피 post밖에 없음. 버튼 누르는거라
    #눌러서 팔로우가 되어 있으면 팔로우 취소/ 아님 팔로우
    me = request.user
    you = get_user_model().objects.get(pk = user_pk)
    if you != me: # 내가 아닐 떄만 확인할 수 있음 / todo
        if me not in you.followers.all():
            you.followers.add(me)
        else: # 이미 팔로우 했으면
            you.followers.remove(me)
    return redirect('accounts:profile',you.id)

            
        
    

