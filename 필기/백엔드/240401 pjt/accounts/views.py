from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm # 사용자 인증과 관련된 Form

from django.contrib.auth import login as auth_login # 로그인 기능 사용하기 위해

from django.contrib.auth import logout as auth_logout # 로그아웃 기능 사용하기 위해


def login(request):
    if request.method == 'POST': # 2. 로그인 버튼을 눌렀으면(갔다 왔으면)
        form = AuthenticationForm(request, request.POST) # 4. 인증폼을 생성하고(request), 로그인 정보를 넣었으면 그 정보를 처리해라(request.POST)
        
        if form.is_valid(): # 5. 유효성 검사
            # create과 달리 얘는 save()할 게 아니라 유효하면 로그인 기능을 사용하면 됨
            auth_login(request,form.get_user()) # 6. 유효하면 사용자 로그인
            return redirect('articles:index') # 7. 기본 페이지로 리다이렉트
        
    else: # 2. POST 요청이 아닐 때(로그인 버튼을 누르기 전), 이거부터 해라. # else부터 처리
        form = AuthenticationForm() # 1. 처음에 로그인 요청을 접근하면(GET요청, 단순 클릭) 로그인을 위한 url로 빈 form과 함께 넘어가면 된다. 
        # 3. 로그인 버튼 누르기 전에는 빈 인증폼 생성
    
    context = {
        'form' : form
    }
    return render(request,'accounts/login.html',context) # 빈 인증폼을 로그인을 위한 html로 보낸다. 이 html은 입력한 정보를 POST 방식으로 다시 해당 함수로 보내줌




# 수정 : 무조건 로그인이 되어있는 상태여야 함

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm


@login_required
def logout(request):
    auth_logout(request) # 사용자 로그아웃
    return redirect('articles:index')

from .forms import UserCreationForm
def signup(request):
    
    #이미 인증된 사용자라면
    if request.user.is_authenticated:
        redirect('articles:index')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # 사용자가 제출한 폼
        if form.is_valid():
            user = form.save() # 유효성 검사 후 DB에 저장
            auth_login(request,user) # 회원가입하자마자 로그인
            return redirect('articles:index')
    
    else:
        form =UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/signup.html',context)
    
@login_required
def delete(request):
    # 현재 로그인 되어 있는 사용자 딜리트
    request.user.delete()
    return redirect('articles:index')  

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form
    }
    return render(request,'accounts/update.html',context)

from django.contrib.auth.forms import PasswordChangeForm # 사용자 인증과 관련된 Form
from django.contrib.auth import update_session_auth_hash # 사용자 세션에 대한 인증 해쉬, 사용자 비밀번호를 변경했을 때 주로 호출, 사용자의 세션 인증에 사용되는 해시가 업데이트 되었을 때 사용
# 사용자 계정 보안을 강화하기 위해 사용

def change_pw(request,user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            
            # 세션의 인증 해시 업데이트
            ###########################
            # 이 부분이 다르다.
            update_session_auth_hash(request,user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request,'accounts/change_pw.html',context)

# from django.contrib.auth.
# def signup(request):
#     form =