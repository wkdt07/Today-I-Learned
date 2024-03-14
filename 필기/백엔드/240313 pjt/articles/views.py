from django.shortcuts import render

# Create your views here.

def index(request):
    
    context = {
        'name' : 'Jane',
        'num' : 1 # details로 이동하기 위해선 num 변수도 필요하다.
    }
    
    
    # render 함수의 3번째 항목에는 매개변수
    return render(request,'articles/index.html',context)

import random
def dinner(request):
    
    foods = ['족발','치킨','보쌈','삼겹살']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked, 
    }
    
    return render(request,'articles/dinner.html',context)

def search(request):
    return render(request,'articles/search.html')

def throw(request):
    return render(request,'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        
        'message' : message
    }
    return render(request,'articles/catch.html',context)

# /articles/1 ---> '1'이라는 값이 num에 전달되어 함수 안에서 num으로 사용(context={'num':num})
def detail(request,num):
    context = {
        'num':num,
    }
    return render(request,'articles/detail.html',context)