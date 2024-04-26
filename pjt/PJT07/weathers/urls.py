
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'weathers'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/',views.index,name = 'index'),
    path('save_data/',views.save_data,name = 'save_data'),
    path('list_data/',views.list_data,name = 'list_data'),
    path('hot-weathers/',views.hot_weathers,name = 'hot_weathers')
]
