from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'weathers'
urlpatterns = [
    path('problem1/', views.pb1 , name = 'pb1'),
    path('problem2/',views.pb2,name = 'pb2'),
    path('problem3/',views.pb3,name = 'pb3'),
    path('problem4/',views.pb4,name = 'pb4'),   
]
