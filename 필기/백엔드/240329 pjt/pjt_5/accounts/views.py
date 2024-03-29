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


def logout(request):
    auth_logout(request) # 사용자 로그아웃
    return redirect('articles:index')