from django.shortcuts import render

# Create your views here.
def index(request):
    work = request.GET.get("work")
    context = {
        'work' : work
    }
    return render(request, 'todos/index.html',context)

def create_todo(request):
   
    return render(request, 'todos/create_todo.html')

# create에서 request 내부에 GET 요소를 만들고, 이걸 index에서 변수화 해서 index.html에서 출력한다.