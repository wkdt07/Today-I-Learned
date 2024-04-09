from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<username>/',views.profile, name = 'profile'), # 이게 '<username>/'로 위에 있으면 모든 링크가 죽어버림. login이나 logout도 username이라 인식해버리기 때문에
    path('<int:user_pk>/follow/',views.follow,name ='follow'), # 먼저 상대방 요청 정보가 팔로우 되어있는 계정에 있는지 여부에 따라 팔로우/언팔로우가 결정됨 ==> 상대방 계정 정보가 필요함
]
