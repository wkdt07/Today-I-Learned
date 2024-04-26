
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('index/',views.index),
    path('save-deposit-products/',views.save_deposit),
    path('deposit-products/',views.list_products),
    path('deposit-product-options/<str:fin_prdt_cd>/',views.option),
    path('deposit-products/top-rate/',views.top_rate),
]
