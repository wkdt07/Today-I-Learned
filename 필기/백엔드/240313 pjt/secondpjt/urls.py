"""
URL configuration for secondpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles/',include('articles.urls')), # 이건 http://127.0.0.1:8000/articles/주소이름/ 형태로 저장됨  
    path('articles/',include('articles.urls')), # 이 상태로 하면 그냥 articles.urls에서 지정해도 됨 http://127.0.0.1:8000/주소이름/  
    path('page/',include('page.urls'))
]
